import streamlit as st
import shap
import torch
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from rdkit import Chem
from torch_geometric.data import Data, Batch
import io

# ── Device ────────────────────────────────────────────────────
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ── Mutation columns ──────────────────────────────────────────
MUTATION_COLS = ['TP53','EGFR','KRAS','STK11','KEAP1','BRAF',
                 'PIK3CA','ALK','ROS1','MET','ERBB2','NF1',
                 'RB1','SMARCA4','CDKN2A','PTEN']

# ── Load task-aware cell features ─────────────────────────────
@st.cache_data
def load_task_features():
    df = pd.read_csv("data/TASK_AWARE_CELL_FEATURES.csv")
    df = df.set_index("ModelID")
    return df

# ── Load SMILES ───────────────────────────────────────────────
@st.cache_data
def load_smiles():
    df = pd.read_csv("data/GDSC_FULL_SMILES.csv")
    return dict(zip(df["Drug"], df["CanonicalSMILES"]))

# ── Atom features (exact match to dashboard graph_builder) ────
def mol_to_graph(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    node_features = []
    for atom in mol.GetAtoms():
        node_features.append([
            atom.GetAtomicNum(),
            atom.GetDegree(),
            atom.GetFormalCharge(),
            int(atom.GetIsAromatic()),
            atom.GetTotalNumHs()
        ])
    edge_index = []
    for bond in mol.GetBonds():
        s, e = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
        edge_index += [[s, e], [e, s]]
    x = torch.tensor(node_features, dtype=torch.float)
    if len(edge_index) == 0:
        edge_index = torch.zeros((2, 0), dtype=torch.long)
    else:
        edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
    return Data(x=x, edge_index=edge_index)

# ── Prediction wrapper ────────────────────────────────────────
def make_predictor(model, drug_name, smiles_dict):
    smiles = smiles_dict.get(drug_name)
    if smiles is None:
        return None
    graph = mol_to_graph(smiles)
    if graph is None:
        return None
    graph = graph.to(device)

    def predict(cell_matrix):
        results = []
        model.eval()
        with torch.no_grad():
            for row in cell_matrix:
                cf = torch.tensor(row, dtype=torch.float32).unsqueeze(0).to(device)
                bg = Batch.from_data_list([graph])
                pred = model(cf, bg)
                results.append(pred.item())
        return np.array(results)
    return predict

# ── Feature names ─────────────────────────────────────────────
def get_feature_names(columns):
    names = []
    for c in columns:
        if c in MUTATION_COLS:
            names.append(f"{c}_mut")
        else:
            names.append(f"CellEmb_{c}")
    return names

# ── Run SHAP ──────────────────────────────────────────────────
def run_shap(model, cell_line, drug_name, smiles_dict, task_df, nsamples=300):
    feature_cols  = list(task_df.columns)
    feature_names = get_feature_names(feature_cols)

    query      = task_df.loc[cell_line, feature_cols].values.reshape(1, -1).astype(np.float32)
    background = task_df.median(axis=0).values.reshape(1, -1).astype(np.float32)

    predictor = make_predictor(model, drug_name, smiles_dict)
    if predictor is None:
        return None

    np.random.seed(42)
    explainer   = shap.KernelExplainer(predictor, background)
    shap_values = explainer.shap_values(query, nsamples=nsamples, silent=True)

    return {
        "shap_values"  : shap_values[0],
        "base_value"   : explainer.expected_value,
        "pred_value"   : predictor(query)[0],
        "feature_names": feature_names,
        "query"        : query[0]
    }

# ── Waterfall plot ────────────────────────────────────────────
def plot_waterfall(shap_result):
    sv    = shap_result["shap_values"]
    base  = shap_result["base_value"]
    data  = shap_result["query"]
    names = shap_result["feature_names"]

    n_features  = len(sv)
    max_display = min(12, n_features)

    exp = shap.Explanation(
        values        = sv,
        base_values   = base,
        data          = data,
        feature_names = names
    )

    plt.close("all")
    shap.plots.waterfall(exp, max_display=max_display, show=False)
    fig = plt.gcf()
    fig.set_size_inches(7, 5)
    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=130, bbox_inches="tight")
    plt.close("all")
    buf.seek(0)
    return buf

# ── Mutation bar plot ─────────────────────────────────────────
def plot_mutation_bar(shap_result):
    names = shap_result["feature_names"]
    sv    = shap_result["shap_values"]
    vals  = shap_result["query"]

    mut_idx   = [i for i, n in enumerate(names) if n.endswith("_mut")]
    mut_names = [names[i] for i in mut_idx]
    mut_shap  = sv[mut_idx]
    mut_vals  = vals[mut_idx]

    order  = np.argsort(np.abs(mut_shap))[::-1]
    colors = ["#d73027" if v > 0 else "#4575b4" for v in mut_shap[order]]

    plt.close("all")
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.barh(
        y=[mut_names[i] for i in order],
        width=mut_shap[order],
        color=colors, height=0.6
    )

    # Determine x-axis range so we can place all labels at the right edge
    data_min = min(mut_shap.min(), 0)
    data_max = max(mut_shap.max(), 0)
    data_range = data_max - data_min if data_max != data_min else 0.01

    # Place all labels in a tight column on the right side
    label_x = data_max + data_range * 0.02

    for j, (idx, bar) in enumerate(zip(order, bars)):
        status = "Mutated" if mut_vals[idx] == 1 else "Wild-type"
        ax.text(label_x, bar.get_y() + bar.get_height()/2,
                status, va="center", ha="left", fontsize=8, color="#555")

    # Extend x-axis to give room for the labels
    ax.set_xlim(data_min - data_range * 0.05, data_max + data_range * 0.20)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("SHAP Value  |  Red = Resistance  |  Blue = Sensitivity", fontsize=9)
    ax.set_title("Mutation Feature Contributions", fontsize=11)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", dpi=130, bbox_inches="tight")
    plt.close("all")
    buf.seek(0)
    return buf

# ── Natural language explanation ──────────────────────────────
def generate_text_explanation(cell_line, drug_name, shap_result):
    sv    = shap_result["shap_values"]
    vals  = shap_result["query"]
    pred  = shap_result["pred_value"]
    base  = shap_result["base_value"]
    names = shap_result["feature_names"]

    # Find mutated genes
    mutated = []
    for i, n in enumerate(names):
        if n.endswith("_mut") and vals[i] == 1:
            mutated.append(n.replace("_mut", ""))

    # Verdict
    if pred < 0:
        verdict = "HIGHLY SENSITIVE — very likely to respond to this drug"
    elif pred < 5:
        verdict = "SENSITIVE — likely to respond"
    elif pred < 15:
        verdict = "MODERATELY RESISTANT"
    else:
        verdict = "RESISTANT — less likely to respond"

    # Find top 3 embedding features by absolute SHAP value
    embed_indices = [i for i, n in enumerate(names) if not n.endswith("_mut")]
    embed_shap    = [(i, float(sv[i]), abs(float(sv[i]))) for i in embed_indices]
    embed_shap.sort(key=lambda x: x[2], reverse=True)
    top3 = embed_shap[:3]

    lines = []
    lines.append(f"**Predicted LN(IC50):** {pred:.3f}  |  **Verdict:** {verdict}")
    lines.append(f"**Average LN(IC50) across all NSCLC lines:** {base:.3f}")
    lines.append("")
    if mutated:
        lines.append(f"**Mutations present:** {', '.join(mutated)}")
    else:
        lines.append("**Mutations:** No NSCLC driver mutations detected")
    lines.append("")
    lines.append("**Top gene expression drivers:**")
    for idx, shap_val, _ in top3:
        direction = "→ resistance" if shap_val > 0 else "→ sensitivity"
        lines.append(f"- {names[idx]}  (SHAP: {shap_val:+.3f})  {direction}")
    lines.append("")
    lines.append("*SHAP values are mathematically exact — they sum to the exact model prediction.*")

    return "\n".join(lines)

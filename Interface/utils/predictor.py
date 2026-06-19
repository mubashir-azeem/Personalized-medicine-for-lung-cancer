import torch
import pandas as pd

from torch_geometric.data import Batch

from models.model import DrugResponseGNN
from utils.graph_builder import mol_to_graph



# Device
device = torch.device(
    "cuda" if torch.cuda.is_available()
    else "cpu"
)


# Load trained model
model = DrugResponseGNN().to(device)

model.load_state_dict(
    torch.load(
        "models/BEST_END_TO_END_DRUG_GNN_230_EPOCHS.pth",
        map_location=device
    )
)

model.eval()


# Load datasets
cell_df = pd.read_csv(
    "data/TASK_AWARE_CELL_FEATURES.csv"
)

smiles_df = pd.read_csv(
    "data/GDSC_FULL_SMILES.csv"
)


# Build drug graph cache
drug_graphs = {}

for _, row in smiles_df.iterrows():

    graph = mol_to_graph(
        row["CanonicalSMILES"]
    )

    if graph is not None:

        drug_graphs[
            row["Drug"]
        ] = graph

def effectiveness_label(ic50):

    if ic50 <= -4:
        return "⭐⭐⭐⭐⭐ Very High"

    elif ic50 <= -3:
        return "⭐⭐⭐⭐ High"

    elif ic50 <= -2:
        return "⭐⭐⭐ Moderate"

    elif ic50 <= -1:
        return "⭐⭐ Low"

    else:
        return "⭐ Very Low"


# Prediction function
def predict_drugs_for_cell(selected_cell):

    cell_row = cell_df[
        cell_df["ModelID"] == selected_cell
    ]

    if len(cell_row) == 0:

        raise ValueError(
            f"{selected_cell} not found."
        )

    cell_features = torch.tensor(
        cell_row.drop(
            columns=["ModelID"]
        ).values,
        dtype=torch.float32
    ).to(device)

    results = []

    with torch.no_grad():

        for drug_name, graph in drug_graphs.items():

            graph_batch = Batch.from_data_list(
                [graph]
            ).to(device)

            pred_ic50 = model(
                cell_features,
                graph_batch
            ).item()

            results.append({
                "Drug": drug_name,
                "Predicted_LN_IC50": pred_ic50
            })

    results_df = pd.DataFrame(
        results
    )

    results_df = results_df.sort_values(
        "Predicted_LN_IC50",
        ascending=True
    )

    results_df.reset_index(
        drop=True,
        inplace=True
    )

    return results_df


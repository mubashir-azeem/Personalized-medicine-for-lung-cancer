import pandas as pd


def load_cell_features():

    return pd.read_csv(
        "data/TASK_AWARE_CELL_FEATURES.csv"
    )


def load_smiles():

    return pd.read_csv(
        "data/GDSC_FULL_SMILES.csv"
    )


def load_expression():

    return pd.read_csv(
        "data/FINAL_NSCLC_EXPRESSION.csv"
    )


def load_mutations():

    return pd.read_csv(
        "data/CCLE_mutations.csv"
    )
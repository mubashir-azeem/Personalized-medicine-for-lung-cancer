import torch

from rdkit import Chem

from torch_geometric.data import Data


def mol_to_graph(smiles):

    mol = Chem.MolFromSmiles(
        smiles
    )

    if mol is None:
        return None

    node_features = []

    for atom in mol.GetAtoms():

        node_features.append([

            atom.GetAtomicNum(),

            atom.GetDegree(),

            atom.GetFormalCharge(),

            int(
                atom.GetIsAromatic()
            ),

            atom.GetTotalNumHs()

        ])

    edge_index = []

    for bond in mol.GetBonds():

        start = bond.GetBeginAtomIdx()

        end = bond.GetEndAtomIdx()

        edge_index.append(
            [start, end]
        )

        edge_index.append(
            [end, start]
        )

    x = torch.tensor(
        node_features,
        dtype=torch.float
    )

    edge_index = torch.tensor(
        edge_index,
        dtype=torch.long
    ).t().contiguous()

    return Data(
        x=x,
        edge_index=edge_index
    )
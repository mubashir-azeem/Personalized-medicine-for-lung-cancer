# Model Files Overview

The trained models used in this project are stored in a separate Google Drive folder because several model files exceed GitHub's file size limitations.

**Models Folder:**

[Google Drive Model Repository](https://drive.google.com/drive/folders/1vq-ROTVhVxD2v3meomT2oKiHIAjRam3r?usp=sharing&utm_source=chatgpt.com)

## Available Models

| Model File                                | Size     | Description                                                                        |
| ----------------------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `task_aware_encoder.keras`                | 74.2 MB  | Encoder model used to generate task-aware feature representations.                 |
| `task_aware_autoencoder.keras`            | 445.7 MB | Autoencoder trained to learn task-aware representations from cancer cell features. |
| `pretrained_encoder.keras`                | 74.3 MB  | Pretrained encoder used during feature extraction and representation learning.     |
| `Final_NSCLC_Drug_Response_Model.keras`   | 14 MB    | Final deep learning model developed for NSCLC drug response prediction.            |
| `END_TO_END_DRUG30_GNN.pth`               | 2.1 MB   | Graph Neural Network model checkpoint trained for 30 epochs.                       |
| `END_TO_END_DRUG_GNN_130_EPOCHS.pth`      | 2.1 MB   | Graph Neural Network model checkpoint trained for 130 epochs.                      |
| `END_TO_END_DRUG_GNN_190_EPOCHS.pth`      | 2.1 MB   | Graph Neural Network model checkpoint trained for 190 epochs.                      |
| `BEST_END_TO_END_DRUG_GNN_230_EPOCHS.pth` | 2.1 MB   | Best-performing Graph Neural Network model checkpoint trained for 230 epochs.      |
| `best_autoencoder.keras`                  | 445.2 MB | Best-performing autoencoder selected after model evaluation.                       |

## Notes

* These files contain the pretrained and fully trained models used throughout the project.
* Multiple checkpoints are provided to allow reproducibility and performance comparison.
* Download the required model files from the Google Drive repository before running the prediction pipeline or reproducing the experiments.

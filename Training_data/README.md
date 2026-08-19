# Training Dataset Overview

The complete training datasets used for model development and training are stored in a separate Google Drive folder because several files exceed GitHub's file size limitations.

**Training Data Folder:**

**https://drive.google.com/drive/folders/1YitT_smXknt6Bbs8I6LZiaRI6u-xkqJi?usp=sharing**

## Available Datasets

| Dataset                           | Size    | Description                                                                                    |
| --------------------------------- | ------- | ---------------------------------------------------------------------------------------------- |
| `TRAINING_FULL.csv`               | 87.1 MB | Complete training dataset containing the processed features used for drug response prediction. |
| `TRAINING_FULL_TASK_AWARE.csv`    | 90.6 MB | Training dataset containing task-aware features generated for the Graph Neural Network model.  |
| `MUTATION_MATRIX.csv`             | 4 KB    | Binary mutation matrix representing genomic mutation information for NSCLC cell lines.         |
| `CELL_FEATURES_WITH_MUTATION.csv` | 153 KB  | Cell feature dataset combining genomic features with mutation information.                     |

## Notes

* The datasets are provided separately because of their large file sizes.
* These files were used during feature engineering, model development, and model training.
* Download all files from the Google Drive folder before running the training pipeline.

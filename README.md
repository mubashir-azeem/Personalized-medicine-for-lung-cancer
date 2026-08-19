# Personalized Medicine for Lung Cancer: AI-Powered Drug Response Prediction and Personalized Drug Recommendation Framework

An artificial intelligence framework for predicting drug responses in **Non-Small Cell Lung Cancer (NSCLC)** using **Graph Neural Networks (GNNs)**. This repository contains the datasets, embeddings, trained models, notebooks, dashboard, and supporting resources used throughout the research and development process.

---

## Repository Structure

```text
├── Dashboard/
│   └── Streamlit dashboard and user interface
│
├── Embeddings/
│   └── Generated embedding datasets
│
├── Notebooks/
│   └── Jupyter notebooks for data analysis and model development
│
├── Raw_data/
│   └── Original datasets used in the project
│
├── Results/
│   └── Model outputs and evaluation results
│
├── Training_data/
│   └── Processed datasets used for model training
│
└── models/
    └── Trained machine learning and Graph Neural Network models
```

---

## Project Components

### Raw Data

Contains the original datasets collected from multiple biomedical sources, including:

* Gene expression data
* Drug response data
* Mutation data
* Molecular structure data (SMILES)
* Metadata for NSCLC cell lines

**Dataset Repository:**

[Raw Data Folder](https://drive.google.com/drive/folders/1wPDx0PoiPiIfu5iIh4B1nccoOM-7aMxd?usp=sharing&utm_source=chatgpt.com)

---

### Training Data

Contains the processed datasets used during model development and training, including:

* Complete training datasets
* Task-aware training datasets
* Mutation matrices
* Combined cell features

---

### Embeddings

Contains the vector representations generated during feature engineering, including:

* Drug embeddings
* Cancer embeddings
* Task-aware embeddings
* Cell feature embeddings

---

### Models

Contains the pretrained and fully trained models used for drug response prediction, including:

* Autoencoders
* Encoders
* Deep learning models
* Graph Neural Network checkpoints

**Model Repository:**

[Models Folder](https://drive.google.com/drive/folders/1vq-ROTVhVxD2v3meomT2oKiHIAjRam3r?usp=sharing&utm_source=chatgpt.com)

---

### Dashboard

Contains the Streamlit-based application developed for data visualization and personalized drug prediction.

**Dashboard Repository:**

[Dashboard Folder](https://drive.google.com/drive/folders/1rjcZ8NnBuPrDv_eJR26TrfpKKO0-g1hv?usp=sharing&utm_source=chatgpt.com)

---

## Data Sources

* Cancer Cell Line Encyclopedia (CCLE)
* Genomics of Drug Sensitivity in Cancer (GDSC)
* DepMap

---

## Technologies

* Python
* PyTorch
* PyTorch Geometric
* RDKit
* Scikit-learn
* Pandas
* NumPy
* Streamlit
* Jupyter Notebook

---

## Author

**Mubashir Azeem Abbasi**

Department of Computer Science

IQRA University

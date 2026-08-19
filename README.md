# Personalized Medicine for Lung Cancer: AI-Powered Drug Response Prediction and Personalized Drug Recommendation Framework

An artificial intelligence framework for predicting drug responses in **Non-Small Cell Lung Cancer (NSCLC)** using **Graph Neural Networks (GNNs)**. This repository contains the datasets, embeddings, trained models, notebooks, the Streamlit dashboard, project walkthrough materials, and supporting resources used throughout the research and development process.

---

## Repository Structure

```text
├── Dashboard/
│   └── Streamlit dashboard, source code, utilities, assets, and interface components
│
├── Embeddings/
│   └── Drug, cancer, and task-aware embedding datasets
│
├── Notebooks/
│   └── Jupyter notebooks for preprocessing, analysis, experimentation, and model development
│
├── Project_walkthrough/
│   └── Video walkthrough explaining the complete project workflow
│
├── Raw_data/
│   └── Original datasets collected from biomedical databases
│
├── Results/
│   └── Predictions, evaluation metrics, visualizations, and experimental results
│
├── Training_data/
│   └── Processed datasets prepared for model training
│
└── models/
    └── Pretrained models, autoencoders, and Graph Neural Network checkpoints
```

---

## Project Components

### Raw Data

Contains the original datasets collected from multiple biomedical resources, including:

* Gene expression datasets
* Drug response datasets
* Mutation datasets
* Drug molecular structures (SMILES)
* NSCLC metadata and cell line information

**Dataset Repository:**

[Raw Data Folder](https://drive.google.com/drive/folders/1wPDx0PoiPiIfu5iIh4B1nccoOM-7aMxd?usp=sharing)

---

### Training Data

Contains the processed datasets generated during preprocessing and feature engineering, including:

* Complete training datasets
* Task-aware training datasets
* Mutation matrices
* Cell feature datasets integrated with mutation information

---

### Embeddings

Contains the vector representations generated during feature extraction and representation learning, including:

* Drug embeddings
* Cancer embeddings
* Task-aware cancer embeddings
* Task-aware cell feature embeddings

---

### Models

Contains the pretrained and fully trained models developed during experimentation, including:

* Autoencoders
* Encoders
* Drug response prediction models
* Graph Neural Network checkpoints

**Model Repository:**

[Models Folder](https://drive.google.com/drive/folders/1vq-ROTVhVxD2v3meomT2oKiHIAjRam3r?usp=sharing)

---

### Dashboard

Contains the complete Streamlit-based application developed for data exploration, visualization, and personalized drug prediction.

The dashboard includes:

* Drug explorer
* Prediction interface
* Model information pages
* Visualization components
* Supporting utilities and assets

**Dashboard Repository:**

[Dashboard Folder](https://drive.google.com/drive/folders/1rjcZ8NnBuPrDv_eJR26TrfpKKO0-g1hv?usp=sharing)

---

### Notebooks

Contains Jupyter notebooks used throughout the project for:

* Data preprocessing
* Dataset integration
* Exploratory data analysis
* Feature engineering
* Model development
* Model training
* Performance evaluation

---

### Results

Contains the outputs generated during experimentation, including:

* Drug response predictions
* Performance metrics
* Model evaluation results
* Generated visualizations
* Experimental outputs

---

### Project Walkthrough

Contains a video-based explanation of the complete project implementation.

The walkthrough covers:

* Data collection
* Preprocessing
* Feature engineering
* Embedding generation
* Model development
* Graph Neural Network architecture
* Training pipeline
* Dashboard demonstration
* Personalized drug recommendation workflow

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
* TensorFlow
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

# Dashboard Overview

The complete dashboard source code and supporting files are stored in a separate Google Drive folder.

**Dashboard Folder:**

[Google Drive Dashboard Repository](https://drive.google.com/drive/folders/1rjcZ8NnBuPrDv_eJR26TrfpKKO0-g1hv?usp=sharing&utm_source=chatgpt.com)

## Project Structure

| File/Folder         | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `.streamlit/`       | Streamlit configuration files.                                   |
| `assets/`           | Images, icons, and other static resources used by the dashboard. |
| `data/`             | Input datasets required by the application.                      |
| `models/`           | Trained machine learning and Graph Neural Network models.        |
| `other interfaces/` | Additional interface components and supporting modules.          |
| `outputs/`          | Generated predictions, results, and exported files.              |
| `pages/`            | Individual Streamlit dashboard pages.                            |
| `utils/`            | Utility functions and helper modules.                            |
| `Homepage.py`       | Main application entry point for the dashboard.                  |
| `requirements.txt`  | List of Python dependencies required to run the application.     |
| `test.py`           | Testing script for validating dashboard functionality.           |

## Notes

* The dashboard was developed using Streamlit.
* The application integrates datasets, embeddings, trained models, and prediction modules into a single interface.
* Download the complete dashboard folder from the Google Drive repository before running the application.

## Running the Dashboard

```bash
pip install -r requirements.txt
streamlit run Homepage.py
```

from dataclasses import dataclass

@dataclass
class AppConfig:
    UPLOADED_CSV_PATH = "data/uploads/uploaded_csv.csv"
    NOTEBOOK_PATH = "notebooks/session.ipynb"
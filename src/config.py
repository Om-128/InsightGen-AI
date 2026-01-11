from dataclasses import dataclass

'''
    Data class helps us to manage file paths
'''
@dataclass
class AppConfig:
    UPLOADED_CSV_PATH = "data/uploads/uploaded_csv.csv"
    NOTEBOOK_BASE_PATH = "data/generated_notebook"
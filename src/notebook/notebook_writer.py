import os
import sys
from datetime import datetime

from src.config import AppConfig
from src.Custome_Exception import CustomException

import nbformat
from nbformat.v4 import new_notebook
from nbformat.v4 import new_markdown_cell, new_code_cell

'''
    This function creates a new notebook file in generated_notebook/ folder for every session
    Returns notebook file path
'''
def create_new_notebook(base_path: str) -> str:
    """
    Creates a new empty Jupyter notebook and returns its path
    """
    os.makedirs(base_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    notebook_name = f"eda_notebook_{timestamp}.ipynb"

    notebook_path = os.path.join(base_path, notebook_name)

    nb = new_notebook(cells=[])
    with open(notebook_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    return notebook_path

'''
    This function is called from frontend
    It appends question and code to the notebook 
'''
def append_to_notebook(path, question, code):

    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        raise CustomException(e, sys)
    
    nb.cells.append(new_markdown_cell(f"\n{question}"))
    nb.cells.append(new_code_cell(code))

    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

'''
    This is a helper function which extracts the last line from the code
    Remove uncessarry code lines
'''
def extract_final_line(code: str) -> str:
    lines = [
        line.strip()
        for line in code.splitlines()
        if line.strip()
    ]
    return lines[-1]

'''
    This function adds initial imports to the notebook when new notebook is created
'''
def get_initial_imports():
    initial_comment = "Starter Imports"
    initial_imports = (
    "import pandas as pd\n"
    "import numpy as np\n"
    "import seaborn as sns\n"
    "import matplotlib.pyplot as plt\n"
    "df = pd.read_csv('Enter your data file path')\n"
    )

    return initial_comment, initial_imports

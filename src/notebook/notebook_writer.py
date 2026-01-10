import os
import sys
from datetime import datetime

from src.config import AppConfig
from src.Custome_Exception import CustomException

import nbformat
from nbformat.v4 import new_notebook
from nbformat.v4 import new_markdown_cell, new_code_cell

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

def append_to_notebook(path, question, code):

    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        raise CustomException
    
    nb.cells.append(new_markdown_cell(f"### Question\n{question}"))
    nb.cells.append(new_code_cell(code))

    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

def extract_final_line(code: str) -> str:
    lines = [
        line.strip()
        for line in code.splitlines()
        if line.strip()
    ]
    return lines[-1]

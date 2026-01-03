import os
import sys

from src.config import AppConfig
from src.Custome_Exception import CustomException

import nbformat
from nbformat.v4 import new_markdown_cell, new_code_cell

def append_to_notebook(path, question, code):

    try:
        nb = nbformat.read(path, as_version=4)
    except Exception as e:
        raise CustomException
    
    nb.cells.append(new_markdown_cell(f"### Question\n{question}"))
    nb.cells.append(new_code_cell(code))

    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

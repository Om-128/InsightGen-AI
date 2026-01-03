import os
import sys

import pandas as pd

from src.Custome_Exception import CustomException

from src.llm.create_pandas_agent import AgentManager
from src.notebook.notebook_writer import append_to_notebook
from src.config import AppConfig

if __name__=="__main__":
    
    app_config = AppConfig()
    agent_manager = AgentManager()

    csv_path = app_config.UPLOADED_CSV_PATH
    llm = agent_manager.create_model()

    df = pd.read_csv(csv_path)

    pandas_agent = agent_manager.create_pandas_agent(model=llm, df=df)
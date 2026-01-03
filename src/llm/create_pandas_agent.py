import os
import sys

import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_experimental.agents import create_pandas_dataframe_agent

from src.config import AppConfig
from src.Custome_Exception import CustomException

''' 
    This class createes an model and then creates an pandas dataframe agent
'''
class AgentManager:

    def create_model(self):
        try:
            llm = OllamaLLM(model="llama3.1:8b")
            print("Model created successfully...")
            return llm
        except Exception as e:
            raise CustomException(e, sys)

    def create_pandas_agent(self, model, df):
        try:
            pandas_agent = create_pandas_dataframe_agent(
                model,
                df,
                verbose=False,
                allow_dangerous_code=True,
                return_intermediate_steps=True
            )

            print("Pandas agent created successfully...Using")
            return pandas_agent
        except Exception as e:
            raise CustomException(e, sys)
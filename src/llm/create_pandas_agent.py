import os
import sys

import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_experimental.agents import create_pandas_dataframe_agent

from src.Custome_Exception import CustomException
from dataclasses import dataclass

'''
    This class holds the uploaded csv file location
'''
@dataclass
class PandasAgentConfig:
    uploaded_csv_path = r'data/uploads/uploaded_csv.csv'

''' 
    This class createes an model and then creates an pandas dataframe agent
'''
class CreatePandasAgent:

    def __init__(self):
        self.config = PandasAgentConfig()
        self.df = pd.read_csv(self.config.uploaded_csv_path)

    def create_model(self):
        try:
            llm = OllamaLLM(model="llama3.1:8b")
            print("Model created successfully...")
            return llm
        except Exception as e:
            raise CustomException(e, sys)

    def create_pandas_agent(self, model):
        try:
            pandas_agent = create_pandas_dataframe_agent(
                model,
                self.df,
                # verbose=True,
                allow_dangerous_code=True
            )
            print("Pandas agent created successfully...")
            return pandas_agent
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":

    create_pandas_agent = CreatePandasAgent()

    model = create_pandas_agent.create_model()

    pandas_agent = create_pandas_agent.create_pandas_agent(model=model)

    response = pandas_agent.invoke("How many rows are in the dataset?")
    print(response)
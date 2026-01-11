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

    '''
        This function creates the llm model locally
    '''
    def create_model(self):
        try:
            llm = OllamaLLM(
                model="llama3.1:8b",
                system="""
You are a Pandas DataFrame analysis agent.
You MUST answer by executing pandas code.
DO NOT ask questions.
DO NOT respond in plain English.
Always use the dataframe tool.
"""
                )
            print("Model created successfully...")
            return llm
        except Exception as e:
            raise CustomException(e, sys)

    '''
        This function creates pandas agent
    '''
    def create_pandas_agent(self, model, df):
        try:
            pandas_agent = create_pandas_dataframe_agent(
                model,
                df,
                verbose=True,
                allow_dangerous_code=True,
                return_intermediate_steps=True,
                handle_parsing_errors=True 
            )

            print("Pandas agent created successfully...Using")
            return pandas_agent
        except Exception as e:
            raise CustomException(e, sys)

    '''
        This function is responsible for formatting Agent response
        Removes unnecessary line and only returns code and response
    '''
    def format_agent_response(self, result):
        """Extracts code and final answer from agent response."""
        
        # Start with empty lists and strings
        code_blocks = []
        output = ""
        
        # If response has intermediate steps
        if 'intermediate_steps' in result:
            steps = result['intermediate_steps']
            
            # Loop through each action + result pair
            for action, observation in steps:
                # Get code from action (remove backticks)
                code = str(action.tool_input).strip("`")
                if code:
                    code_blocks.append(code)
        
        # Get final answer from response
        output = result.get('output', '')
        
        # Join all code blocks
        code_str = "\n".join(code_blocks) if code_blocks else "No code executed"
        
        return code_str, output
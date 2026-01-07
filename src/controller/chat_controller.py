import sys
from src.Custome_Exception import CustomException

class ChatController:
    def __init__(self, agent):
        self.agent = agent

    def ask(self, question: str) -> str:
        try:
            response = self.agent.invoke(question)

            return response

        except Exception as e:
            raise CustomException(e, sys)
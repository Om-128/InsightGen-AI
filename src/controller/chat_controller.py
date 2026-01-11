import sys
from src.Custome_Exception import CustomException

class ChatController:
    def __init__(self, agent):
        self.agent = agent

    '''
        This function is called by llm from fronted
    '''
    def ask(self, question: str) -> str:
        try:
            response = self.agent.invoke(
                {"input": question}
            )
            return response

        except Exception as e:
            return {
                "output": (
                    "⚠️ I couldn't parse the model response for this question.\n\n"
                    "Try asking it in a more explicit way, for example:\n"
                    "- 'Find the minimum and maximum release_year'\n"
                    "- 'Show earliest and latest release year using pandas'\n"
                ),
                "intermediate_steps": []
            }
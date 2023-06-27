import openai
from langchain.llms import OpenAI

class Question:
    #Receive a problem from the LLM
    def problem(interests, topic, llm):
        prompt = f"""
            I need a practice math question for a high school student. Please generate a problem (and only the problem)
            including required formulas about {topic} that can relate to the students interest of {interests}.
        """
        return llm.predict(prompt)
import openai
from langchain.llms import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class Question:
    #Receive a problem from the LLM
    def problem(interests, topic, llm):
        prompt = f"""
            I need a practice math question for a high school student. Please generate a problem (and only the problem),
            including required formulas, about {topic} that can relate to the students interest of {interests}.
            Please ensure that the solution contains only one number, and without units. 
            """
        return llm.predict(prompt)
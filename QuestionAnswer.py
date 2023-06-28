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
    
    def check_answer(question, llm):
        prompt = f"""
        Given the below math question, return the answer to the question and only the answer (no labelling or units please). Only return the answer if it is positive.
        {question}
        """
        answer = llm.predict(prompt)
        return answer
import openai
from langchain.llms import OpenAI
import os
import math

openai.api_key = os.getenv("OPENAI_API_KEY")

class QuestionAnswer:
    def check_answer(question, response, llm):
        prompt = f"""
        Given the below math question, return the answer to the question and only the answer (no labelling or units please). Only return the answer if it is positive.
        {question}
        """
        answer = llm.predict(prompt)
        correct = float(answer) == float(response)
        return correct, answer
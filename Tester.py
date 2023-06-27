from Question import Question
from QuestionAnswer import QuestionAnswer
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
import openai, os

# openai.organization = "org-64LJ5L34voPi4VOssqyzlQAk"

llm = OpenAI(temperature=0.7)
question = Question.problem("bicycles", "solving quadratic equations", llm)
print(question)
response = input()
(correct, answer) = QuestionAnswer.check_answer(question, response, llm)
if correct:
    print("Correct!")
else:
    print("Incorrect")
print(f"You answered: {response}")
print(f"Correct answer: {answer}")
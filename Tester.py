from Question import Question
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

llm = OpenAI(temperature=0.7)
x = Question.problem("bicycles", "solving quadratic equations", llm)
print(x)
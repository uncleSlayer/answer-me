from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_template(
    "Write a poem about {topic} in 20 words at max. Keep in mind the word count"
)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
)

app = FastAPI(
    title="ASK ME ANYTHING poet",
    description="Ask me anything",
    version="1.0.0",
)

add_routes(app, prompt | llm, path="/poet")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

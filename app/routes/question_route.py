from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.questions import prompt_template as question_prompt_template
from app.ai import openAiClient, astra_vector_store
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


class Ask_Question(BaseModel):
    question: str


question_router = APIRouter()


@question_router.post("/ask")
async def ask_question(request_body: Ask_Question):

    question = request_body.question

    chain = question_prompt_template | openAiClient | StrOutputParser()

    answer = chain.invoke({"question": question})

    print(answer)

    return {"question": answer}

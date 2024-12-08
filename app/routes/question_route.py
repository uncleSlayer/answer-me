from fastapi import APIRouter
from pydantic import BaseModel
from app.ai.questions import prompt_template as question_prompt_template
from app.ai import openAiClient
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from app.ai import chroma_vector_store


class Ask_Question(BaseModel):
    question: str


question_router = APIRouter()


@question_router.post("/ask")
async def ask_question(request_body: Ask_Question):

    question = request_body.question

    chain = question_prompt_template | openAiClient | StrOutputParser()

    answer = chain.invoke({"question": question})

    print(answer)

    return {"answer": answer}


@question_router.post("/ask-rag")
async def ask_question_rag(request_body: Ask_Question):
    question = request_body.question

    retriver = chroma_vector_store.as_retriever(
        search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.3, "k": 3}
    )

    retrived_documents = retriver.invoke(question)
    formatted_docs = [doc.page_content for doc in retrived_documents]

    if len(formatted_docs) > 0: 

        chain = question_prompt_template | openAiClient | StrOutputParser()

        try:
            answer = chain.invoke({
                "question": question, 
                "documents_page_content": formatted_docs[0]
            })
            
            return {"answer": answer}

        except KeyError as e:
            
            return {"error": str(e)}
    
    else:
        print("No document found")
        return {"error": "No relevant document found"}

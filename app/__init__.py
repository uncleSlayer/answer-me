from fastapi import FastAPI
from app.routes.question_route import question_router

app = FastAPI()
app.include_router(question_router)
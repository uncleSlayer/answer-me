from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from app.configs.env import env_config

chroma_vector_store = Chroma(
    collection_name="computer-engineering",
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
    persist_directory="./chroma",
)

openAiClient = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=env_config.OPENAI_API_KEY,
)

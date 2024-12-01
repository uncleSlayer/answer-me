from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from app.configs.env import env_config

astra_vector_store = AstraDBVectorStore(
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    api_endpoint=env_config.ASTRA_API_ENDPOINT,
    collection_name=env_config.ASTRA_COLLECTION_NAME,
    namespace=env_config.ASTRA_NAMESPACE,
    token=env_config.ASTRA_ACCESS_TOKEN,
)

openAiClient = ChatOpenAI(
    model="gpt-3.5-turbo",
    # openai_api_key=env_config.OPENAI_API_KEY,
)
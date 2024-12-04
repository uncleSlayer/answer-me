from langchain_community.document_loaders import PyPDFLoader
import os
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.ai import chroma_vector_store

script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(
#     script_dir,
#     "../../../Python_Pocket_Reference,_5th_Edition_Python_in_Your_Pocket_PDFDrive.pdf",
# )

# openAiEmbeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)

all_splits = text_splitter.split_documents(docs)

# ids = chroma_vector_store.add_documents(documents=all_splits)


# python3 -m app.ai.embeddings.create
# always run this file with the above command from the root directory of the project otherwise it won't work.
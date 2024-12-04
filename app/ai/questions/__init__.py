from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(
    """
    You are an assistant that summarizes information concisely.
    Answer the question in 20 words or fewer, focusing on relevance and clarity.

    If the answer from vector store is not relevant, then answer the question from your own knowledge.

    Question:
    {question}

    Answer:
    """
)


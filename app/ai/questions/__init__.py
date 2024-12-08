from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["question", "documents_page_content"],
    template="""
        Use the following documents to answer the question. If the documents do not contain enough information, use the documents but add your own knowledge to write a comprehensive answer.

        Documents: {documents_page_content}
        Question: {question}
        Answer:
    """,
)

from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_template(
    """
    Answer the question in max 20 words.
    The word count limit of 20 characters is necessarily enforced.

    <Question>
    {question}
    </Question>
    """
)

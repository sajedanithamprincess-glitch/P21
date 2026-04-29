from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class LLMService:
    def __init__(self, model_name, temperature=0.0):
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)

    def generate_answer(self, query, context_text):
        prompt = f"""
Answer the question using ONLY the context below.

Question:
{query}

Context:
{context_text}

Instructions:
- Use only the information in the documents.
- Cite the source and page number when possible.
- Format citations like this: (Source: document_name, Page: X)

If the answer is not present in the documents, say:
"I don't have enough information in the provided documents."
"""

        messages = [
            SystemMessage(content="You answer only using retrieved documents. Never invent information."),
            HumanMessage(content=prompt),
        ]

        response = self.llm.invoke(messages)
        return response.content
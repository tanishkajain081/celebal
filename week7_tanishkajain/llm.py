from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def generate_answer(question, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the given context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content
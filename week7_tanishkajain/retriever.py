def retrieve_chunks(vector_db, question):
    docs = vector_db.similarity_search(question, k=3)
    return docs
from pypdf import PdfReader
from utils import split_text
from embeddings import get_embedding_model
from vector_store import create_vector_store
from retriever import retrieve_chunks
from llm import generate_answer

# Load PDF
reader = PdfReader("documents/sales resume bhav.pdf")

# Extract text
text = ""

for page in reader.pages:
    extracted_text = page.extract_text()

    if extracted_text:
        text += extracted_text + "\n"

print("PDF Loaded Successfully!")
print("Number of Pages:", len(reader.pages))

# Split text
chunks = split_text(text)

print("Total Chunks:", len(chunks))
print("\nFirst Chunk:\n")
print(chunks[0])

# Load Embedding Model
embeddings = get_embedding_model()

print("\nEmbedding Model Loaded Successfully!")

# Create Vector Database
vector_db = create_vector_store(chunks, embeddings)

print("Vector Database Created Successfully!")

# Ask Question
question = input("\nEnter your question: ")

# Retrieve Relevant Chunks
docs = retrieve_chunks(vector_db, question)

answer = generate_answer(question, docs)

print("\nAnswer:\n")
print(answer)
    
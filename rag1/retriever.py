import chromadb
from sentence_transformers import SentenceTransformer

client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection(name="pdf_rag")

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(question):
    embedding2 = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding2],
        n_results=3,
        include=["documents", "distances"] 
    )
    return results["documents"][0]
text=("how to Escalate. If steps 1-6 do not resolve the issue,")
out=retrieve(text)
for i, doc in enumerate(out):
    print(f"Result {i+1}: {doc}")


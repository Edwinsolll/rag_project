import chromadb
from sentence_transformers import SentenceTransformer

client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection(name="pdf_rag")

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrive(input):
    embedding2 = model.encode(input).tolist()
    results = collection.query(query_embeddings=[embedding2], n_results=3)

    chunks=results['documents'][0]
    return chunks
    


import fitz 
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from sentence_transformers import SentenceTransformer

def extract_text(pdf: str):
    doc = fitz.open(pdf)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

text = extract_text("telecom_guide.pdf")

def splittext(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    text1 = splitter.split_text(text)
    return text1
 
chunks = splittext(text)

client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection(name="pdf_rag")

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(words):
        embeddings = model.encode(words).tolist()
        print(embeddings)
        ids= [str(i) for i in range(len(words))]

        collection.add(
            ids= ids,
            documents= words,
            embeddings = embeddings
        )

embed(chunks)


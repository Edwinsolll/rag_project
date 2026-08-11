import fitz 
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
from sentence_transformers import SentenceTransformer

class Pdfloaderror(Exception):
     pass

def extract_text(pdf: str):
    try:
        doc = fitz.open(pdf)
        fulltext = ""
        for page in doc:
            fulltext += page.get_text()

       
        return fulltext
    except fitz.FileNotFoundError:
        raise Pdfloaderror(
            f"PDF file was not found: {pdf}"
        )

    except fitz.FileDataError:
        raise Pdfloaderror(
            f"Invalid or corrupted PDF: {pdf}"
        )
    except PermissionError:
        raise Pdfloaderror(
            f"Permission denied: {pdf}"
        )
    
    except Exception as e:
        raise Pdfloaderror(
            f"Unexpected error while processing {pdf}"
        ) from e
     
def splittext(text: str):
        splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " ", ""]
        )
        text1 = splitter.split_text(text)
        return text1

def embed(words):
    embeddings = model.encode(words).tolist()
    ids= [str(i) for i in range(len(words))]

    collection.add(
        ids= ids,
        documents= words,
        embeddings = embeddings
        )

try:
    text = extract_text("new.pdf")
    print("PDF extracted successfully!")
    print(len(text), "characters extracted")

except Pdfloaderror as e:
    print(e)
else:
    
    chunks = splittext(text)

    client_db = chromadb.PersistentClient(path="./chroma_db")
    collection = client_db.get_or_create_collection(name="pdf_rag")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embed(chunks)


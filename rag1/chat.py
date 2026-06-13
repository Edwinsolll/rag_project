from sentence_transformers import SentenceTransformer
from groq import Groq
import os
from dotenv import load_dotenv
import retriever

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def answer(question):
    chunks = retriever.retrive(question)
    context = "\n\n".join(chunks)
    
    prompt = f"""Answer the question using only the context below.
            If the answer is not in the context, say "ask relevant question ".  Context: {context}
            Question: {question}
           
                                  """
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
                                                 
   
question = "tell me about international roaming"
print("\n" + answer(question))

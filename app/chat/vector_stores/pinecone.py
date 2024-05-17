
import os
from pinecone import Pinecone
# Updated lib to accomodate for deprecated add_documents and init 
# function of langchain.vectorstores.pinecone
from langchain_pinecone import PineconeVectorStore 
from app.chat.embeddings.openai import embeddings 

# Initialize Pinecone env
api_key = os.environ.get("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENV_NAME")

if not api_key or not environment:
    raise ValueError("PINECONE_API_KEY and PINECONE_ENV_NAME must be set as environment variables.")

pc = Pinecone(
    api_key=api_key,
    environment=environment
)


index_name = os.getenv("PINECONE_INDEX_NAME")
if index_name is None:
    raise ValueError("The environment variable 'PINECONE_INDEX_NAME' is not set.")

# Create or retrieve the Pinecone index
if index_name not in pc.list_indexes().names():
    # Do something if it wasnt there. Probably create it or so. 
    pass


# Langchain wrapper for pinecone
vector_store = PineconeVectorStore(index_name=index_name, 
                                  embedding=embeddings)

def build_retriever(chat_args, k ):
    search_kwargs = {
            "filter": {
                "pdf_id": chat_args.pdf_id
                },
            "k": k
            }
    return vector_store.as_retriever(
            search_kwargs=search_kwargs
            )

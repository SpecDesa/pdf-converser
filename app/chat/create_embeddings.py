from langchain.document_loaders import PyPDFLoader # Load text from pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter # Allow to specify chunks of text
from app.chat.vector_stores.pinecone import vector_store

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    """
    Generate and store embeddings for the given pdf

    1. Extract text from the specified PDF.
    2. Divide the extracted text into manageable chunks.
    3. Generate an embedding for each chunk.
    4. Persist the generated embeddings.

    :param pdf_id: The unique identifier for the PDF.
    :param pdf_path: The file path to the PDF.

    Example Usage:

    create_embeddings_for_pdf('123456', '/path/to/pdf')
    """
    # Init text splitter
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, # 500 char at the time
            chunk_overlap=100,
            )

    # Init loader
    loader = PyPDFLoader(pdf_path)

    # Get docs
    docs = loader.load_and_split(text_splitter)
    print(docs)

    vector_store.add_documents(docs)

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

def create_embeddings(chunks, openai_api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    faiss_index = FAISS.from_texts(chunks, embeddings)
    return faiss_index

def query_documents(query, faiss_index):
    docs = faiss_index.similarity_search(query)
    return docs

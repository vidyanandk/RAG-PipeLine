from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data/AmantyaData")
    store = FaissVectorStore("data/faiss_store")
    store.build_from_documents(docs)
    # store.load()
    #print(store.query("ORGANIZATION FOR INFORMATION SECURITY POLICY?", top_k=3))
    rag_search = RAGSearch()
    # query = "ORGANIZATION FOR INFORMATION SECURITY POLICY?"
    query ="What is exit policies?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)

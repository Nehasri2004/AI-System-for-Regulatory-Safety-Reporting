from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Project paths
BASE = Path(__file__).parent.parent

DB = BASE / "rag_files" / "vectorstore"


# Load ChromaDB
def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=str(DB),
        embedding_function=embeddings
    )

    return db.as_retriever(
        search_kwargs={"k": 3}
    )


# Test retriever
if __name__ == "__main__":

    retriever = get_retriever()

    question = input("Ask a question: ")

    results = retriever.invoke(question)

    for i, doc in enumerate(results):

        print("\n--- Result", i + 1, "---")

        print(doc.page_content[:1000])
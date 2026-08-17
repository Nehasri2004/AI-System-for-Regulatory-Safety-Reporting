from pathlib import Path
import fitz

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


BASE = Path(__file__).parent.parent

REFERENCE = BASE / "reference files"

DB = BASE / "rag_files" / "vectorstore"


def load_pdf(file):

    docs = []

    pdf = fitz.open(file)

    for page in pdf:

        text = page.get_text()

        if text.strip():

            docs.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": str(file)
                    }
                )
            )

    pdf.close()

    return docs


def load_data():

    files = [
        REFERENCE / "PADER_Starter_Guide.pdf",
        REFERENCE / "PADER-FDA-Y0AHP_PADER_Full_sample_data_B-1_CLIENT_DEV_01_FDA_v1_20260810.pdf"
    ]

    docs = []

    for file in files:

        print("Loading:", file.name)

        if not file.exists():

            print("File not found:", file)

            continue

        docs.extend(
            load_pdf(str(file))
        )

    return docs


def split_data(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    return splitter.split_documents(docs)


def create_db(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory=str(DB)
    )

    print("ChromaDB created successfully!")


if __name__ == "__main__":

    docs = load_data()

    print("Pages loaded:", len(docs))

    chunks = split_data(docs)

    print("Chunks created:", len(chunks))

    create_db(chunks)
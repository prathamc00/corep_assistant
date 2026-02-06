from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from chunker import load_and_chunk

# Get the directory where this script is located
BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"
VECTORSTORE_DIR = BASE_DIR / "vectorstore"

def build_vector_store():
    emb = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    docs1 = load_and_chunk(str(DOCS_DIR / "pra_own_funds_instructions.pdf"), "PRA Own Funds")
    docs2 = load_and_chunk(str(DOCS_DIR / "pra_reporting_instructions.pdf"), "PRA Reporting")
    docs3 = load_and_chunk(str(DOCS_DIR / "pra_glossary.pdf"), "PRA Glossary")

    all_docs = docs1 + docs2 + docs3

    vectordb = Chroma.from_documents(
        all_docs,
        embedding=emb,
        persist_directory=str(VECTORSTORE_DIR)
    )

    vectordb.persist()
    print("✅ Vector store created!")

if __name__ == "__main__":
    build_vector_store()

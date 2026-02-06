from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from chunker import load_and_chunk

def build_vector_store():
    emb = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    docs1 = load_and_chunk("../docs/pra_own_funds.pdf", "PRA Own Funds")
    docs2 = load_and_chunk("../docs/pra_reporting_instructions.pdf", "PRA Reporting")
    docs3 = load_and_chunk("../docs/pra_glossary.pdf", "PRA Glossary")

    all_docs = docs1 + docs2 + docs3

    vectordb = Chroma.from_documents(
        all_docs,
        embedding=emb,
        persist_directory="../vectorstore"
    )

    vectordb.persist()
    print("✅ Vector store created!")

if __name__ == "__main__":
    build_vector_store()

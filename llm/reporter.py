from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

import chromadb
from sentence_transformers import SentenceTransformer
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from llm.schema import CorepReport
import json

# Get absolute path to vectorstore
BASE_DIR = Path(__file__).resolve().parent.parent
VECTORSTORE_DIR = BASE_DIR / "vectorstore"

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))
collection = client.get_or_create_collection(name="langchain")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)


prompt = ChatPromptTemplate.from_template("""
You are a regulatory reporting analyst for UK banks.

Use ONLY the provided PRA rule text to determine how the COREP C01.00 Own Funds
fields should be populated.

Regulatory text:
{context}

Scenario:
{scenario}

You must produce output strictly in this JSON schema:

{{
  "template": "C01.00",
  "fields": [
    {{
      "code": "010",
      "name": "Common Equity Tier 1",
      "value": number,
      "justification": "text",
      "rules_used": ["rule references"]
    }}
  ],
  "missing_data": [],
  "validation_flags": []
}}
""")

def generate_report(scenario: str):
    # Generate embedding
    query_embedding = model.encode(scenario).tolist()
    
    # Query Chroma
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )
    
    # Extract documents
    docs = results["documents"][0] if results["documents"] else []
    context = "\n\n".join(docs)

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "scenario": scenario
    })

    return response.content

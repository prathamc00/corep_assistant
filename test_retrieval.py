from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

# Get the vectorstore directory (same folder as this script)
VECTORSTORE_DIR = Path(__file__).resolve().parent

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to the existing Chroma database
client = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))
collection = client.get_or_create_collection(name="langchain")

query = "What qualifies as CET1 capital and what deductions apply?"

# Generate embedding for the query
query_embedding = model.encode(query).tolist()

# Search the collection
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

# Display results
for i, (doc, metadata) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
    print(f"SOURCE: {metadata.get('source', 'Unknown')}")
    print(doc[:500])
    print("\n----\n")

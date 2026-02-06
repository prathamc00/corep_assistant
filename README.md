# COREP Assistant

An AI-powered assistant for generating and validating COREP (Common Reporting) regulatory reports for UK banks. It uses RAG (Retrieval Augmented Generation) to grounding its outputs in official PRA rulebooks.

## Project Status
**Active.** Fully migrated to local Ollama inference.

## Prerequisites
- **Python 3.11** (System Interpreter recommended due to library compatibility)
- **Ollama** running locally (Download from [ollama.com](https://ollama.com))

## Setup
1. **Clone & Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Ensure `langchain-ollama` is installed.*

2. **Pull LLM Model**
   The project is configured to use `llama3.1`. Run this in your terminal:
   ```bash
   ollama pull llama3.1
   ```

3. **Ingest Documents (Optional)**
   The vector store is pre-built in `vectorstore/`. To rebuild it from PDF docs:
   ```bash
   python ingestion/embedder.py
   ```

## Usage
Run the reporter test script to generate a report based on a sample scenario:

```bash
python test_reporter.py
```

### Output
The script will:
1. Embed the input scenario.
2. Retrieve relevant PRA rules from ChromaDB.
3. Query the local Ollama model to generate a JSON report.
4. Render the report as a table.
5. Run validation rules to check for calculation errors.

## Architecture
- **Ingestion**: `PyPDFLoader` -> `RecursiveCharacterTextSplitter` -> `SentenceTransformer` -> `ChromaDB`.
- **Generation**: `ChatOllama` (Llama 3.1) -> JSON Output.
- **Validation**: Python-based rule checking (`validator/rules.py`).

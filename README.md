# LLM-Assisted PRA COREP Reporting Assistant (Prototype)

This project demonstrates an **AI-assisted regulatory reporting system** for UK banks regulated by the **Prudential Regulation Authority (PRA)** under the **COREP** reporting framework.

The prototype focuses on **COREP Template C01.00 — Own Funds** and shows how an LLM can:

* Retrieve relevant PRA Rulebook text (RAG)
* Interpret rules for a reporting scenario
* Generate structured COREP field outputs
* Render a human-readable COREP extract
* Apply validation checks to detect prudential inconsistencies

The system runs **fully offline** using Ollama + Llama 3.1 (no API keys required).

---

## 🧠 What This Prototype Demonstrates

End-to-end flow:

```
User scenario
   ↓
Retrieve PRA rule text (vector RAG)
   ↓
LLM reasoning (local model)
   ↓
Structured COREP JSON output
   ↓
Template rendering
   ↓
Validation engine flags inconsistencies
```

This is not a chatbot — it is a **rule-aware regulatory reporting assistant**.

---

## 🏗️ Architecture

See: `Architecture.png`

## 🔄 Workflow

See: `workflow.png`

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/prathamc00/corep_assistant.git
cd corep_assistant
```

### 2. Create and activate virtual environment

**Windows**

```
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux**

```
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install Ollama and pull model

Download Ollama: [https://ollama.com](https://ollama.com)

Then run:

```
ollama pull llama3.1
```

---

## 📄 Download Required PRA Documents

This project uses PRA Rulebook PDFs as its knowledge base.

These are **not included** in the repo.

Open `docs/README.txt` and download the required PDFs into the `/docs` folder.

---

## 🧱 Build the Vector Store (RAG memory)

After placing the PDFs in `/docs`, run:

```
python ingestion/embedder.py
```

This creates the local `vectorstore/` used for rule retrieval.

---

## ▶️ Run the System

### Test retrieval only (RAG test)

```
python test_retrieval.py
```

### Run full COREP reporting assistant

```
python test_reporter.py
```

---

## ✅ Example Output

```
COREP C01.00 — Own Funds

Code      Field                              Value
------------------------------------------------------------
010       Common Equity Tier 1               65

VALIDATION FLAGS:
- CET1 calculation mismatch. Expected 55 based on deductions, got 65.
```

This demonstrates:

* LLM populates COREP field
* Validation engine detects prudential error

---

## 📁 Project Structure

```
docs/                → Instructions to download PRA PDFs
ingestion/           → PDF chunking & embedding
llm/                 → LLM reporting logic & schema
renderer/            → COREP template view
validator/           → Prudential validation rules

test_retrieval.py    → RAG test
test_reporter.py     → End-to-end demo
```

---

## 🧩 Technologies Used

* Python
* LangChain (modular v1 packages)
* ChromaDB (vector store)
* Sentence Transformers (embeddings)
* Ollama
* Llama 3.1 (local LLM)

---

## 🎯 Key Features

* Retrieval-Augmented Generation over PRA Rulebook
* Schema-constrained COREP output
* Human-readable template rendering
* Validation engine for prudential consistency
* Fully offline execution (no API usage)

---

## 📌 Notes

* `vectorstore/` is not committed (generated locally)
* PRA PDFs are not committed (see `docs/README.txt`)
* No API keys required

---

## 📚 Purpose

This prototype illustrates how LLMs can be safely used in regulated environments with:

* Traceability
* Structured outputs
* Validation safeguards
* Human oversight

PRA DOCUMENTS REQUIRED FOR INGESTION

This project relies on official PRA Rulebook documents as the knowledge base
for Retrieval-Augmented Generation (RAG).

These documents are NOT included in the repository due to their large size.

Before running the ingestion step, download the following PDFs from the
PRA Rulebook website and place them in this /docs folder.

Required documents:

1. Own Funds and Eligible Liabilities (CRR)
   Source: https://www.prarulebook.co.uk
   Save as: pra_own_funds.pdf

2. Reporting (CRR) – Annex II Reporting Instructions
   Source: https://www.prarulebook.co.uk
   Save as: pra_reporting_instructions.pdf

3. PRA Glossary
   Source: https://www.prarulebook.co.uk/glossary
   Save as: pra_glossary.pdf

After placing these files here, run:

    python ingestion/embedder.py

This will build the vectorstore required for the assistant.

 AI System for Regulatory Safety Reporting

 About this Project

This project is an AI-based system for generating regulatory safety reports in pharmacovigilance.

It takes ICSR (Individual Case Safety Report) data, analyzes the safety information, creates evidence, and uses an AI model to generate a PADER (Periodic Adverse Drug Experience Report).

What This Project Does

- Loads ICSR safety data
- Validates and cleans the data
- Analyzes patient and safety information
- Identifies serious cases and adverse events
- Creates safety evidence
- Uses RAG to retrieve relevant evidence
- Uses Groq LLM to generate the final report
- Saves the final PADER safety report

Project Workflow

ICSR Data  
↓  
Data Loading  
↓  
Data Validation  
↓  
Data Analysis  
↓  
Evidence Generation  
↓  
RAG Retrieval  
↓  
AI Model  
↓  
PADER Safety Report

Technologies Used

- Python
- Pandas
- NumPy
- LangChain
- Groq LLM
- ChromaDB
- RAG
- JSON
- Excel

The Project Structure

```text
AI-System-for-Regulatory-Safety-Reporting
│
├── app.py
├── generator.py
├── report.py
├── requirements.txt
│
├── data
│   ├── load_data.py
│   ├── analysis.py
│   └── validator.py
│
├── rag_files
│   ├── evidence.py
│   ├── ingest.py
│   └── retriever.py
│
├── outputs
│   ├── analysis.json
│   ├── evidence.json
│   └── final_pader_report.txt
│
└── reference files

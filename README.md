##AI System for Regulatory Safety Reporting

 1. Project Overview

This project analyzes ICSR pharmacovigilance data and generates a PADER safety report using Python, RAG, ChromaDB, and the Groq LLM.

The system separates data analysis from AI generation. Python performs the important calculations, while the LLM converts the analyzed evidence into a readable report.

2. How to Run

#Install dependencies

pip install -r requirements.txt

3.Architecture

The system follows this flow:

ICSR Excel Dataset
        ↓
Data Loading
        ↓
Data Validation
        ↓
Data Analysis
        ↓
Evidence Generation
        ↓
RAG / ChromaDB
        ↓
Groq LLM
        ↓
Final PADER Report

The Excel data is first loaded and analyzed using Python and Pandas.

The analysis results are converted into structured evidence.

The evidence is then used by the RAG system and provided as context to the Groq LLM.

The LLM generates the final PADER report.

##AI vs Deterministic Code

### Deterministic Code

Python and Pandas are used for:

- Loading data
- Validating data
- Counting cases
- Finding serious cases
- Analyzing demographics
- Analyzing adverse events
- Analyzing outcomes
- Creating evidence

These calculations are done using code because numerical safety information should be consistent and reproducible.

# AI

The Groq LLM is used for:

- Summarizing the evidence
- Organizing the report
- Writing the final PADER report

The LLM is not used to calculate the original numbers.

This split keeps the important calculations deterministic while using AI for natural-language generation.

## Prompt and Context

The system uses the following prompt:

You are a pharmacovigilance assistant.

Create a PADER safety report using only
the evidence below.

Do not invent facts or numbers.

Include:

1. Executive Summary
2. Case Summary
3. Serious Case Summary
4. Demographic Summary
5. Adverse Event Summary
6. Outcome Summary
7. Safety Findings
8. PADER Guidance
9. Conclusion

EVIDENCE:

The evidence is dynamically added to the prompt before sending it to the Groq LLM.

## How the System Stays Grounded

The grounding process is:

Original Data
     ↓
Python Analysis
     ↓
Evidence
     ↓
RAG Retrieval
     ↓
LLM Context
     ↓
Final Report

The system calculates important values using Python.

These results are stored as evidence and provided to the LLM.

The prompt also tells the LLM:

"Use only the evidence provided and do not invent facts or numbers."

This reduces hallucinations and keeps the report connected to the analyzed data.

The current version does not automatically attach an evidence citation to every generated sentence. Therefore, the final report should be reviewed against the evidence before regulatory use.

## Evaluation at Scale

Instead of testing only one report, the system can be tested with 1,000 generated reports.
The reports can be evaluated using:
- Numerical Accuracy
- Grounded Claim Rate
- Unsupported Claim Rate
- Report Completeness
- Report Consistency
- Generation Time
- Failure Rate
The numbers in the generated reports can be compared with the deterministic Python analysis to check whether the AI output is correct.

## Known Limitations

- The current project uses a sample dataset.
- More testing is required with larger datasets.
- The LLM may still generate unsupported statements.
- Sentence-level evidence citations are not implemented yet.
- Human review is still required before regulatory use.
- The project iAI System for Regulatory Safety Reporting


##Structure of project
├── app.py
├── generator.py
├── report.py
├── requirements.txt
├── Bisoprolol_icsr_sample_1068rows.xlsx
│
├── data/
│   ├── load_data.py
│   ├── analysis.py
│   └── validator.py
│
├── rag_files/
│   ├── evidence.py
│   ├── ingest.py
│   └── retriever.py
│
├── outputs/
│   ├── analysis.json
│   ├── evidence.json
│   ├── final_pader_report.txt
│   └── final_pader_report.docx
│
└── README.mds a prototype and does not replace professional regulatory review.


import json
from pathlib import Path

from rag_files.retriever import get_retriever


# Project paths
BASE = Path(__file__).parent.parent

ANALYSIS_FILE = BASE / "outputs" / "analysis.json"

OUTPUT_FILE = BASE / "outputs" / "evidence.json"


# Load analysis results
def load_analysis():

    with open(ANALYSIS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Get PADER guidance from RAG
def get_guidance(question):

    retriever = get_retriever()

    results = retriever.invoke(question)

    guidance = []

    for doc in results:

        guidance.append({
            "text": doc.page_content,
            "source": doc.metadata.get("source", "unknown")
        })

    return guidance


# Create evidence packet
def create_evidence():

    analysis = load_analysis()

    questions = [
        "What should be included in a PADER report?",
        "How should the narrative summary be written?",
        "How should adverse reactions be analyzed?",
        "How should serious cases be summarized?"
    ]

    evidence = {
        "analysis_results": analysis,
        "pader_guidance": {}
    }

    for question in questions:

        print("Retrieving:", question)

        evidence["pader_guidance"][question] = (
            get_guidance(question)
        )

    return evidence


# Save evidence
if __name__ == "__main__":

    evidence = create_evidence()

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            evidence,
            file,
            indent=4
        )

    print("\nEvidence created successfully!")

    print(
        "Saved at:",
        OUTPUT_FILE
    )
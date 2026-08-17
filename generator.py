import json
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()


BASE = Path(__file__).parent
EVIDENCE = BASE / "outputs" / "evidence.json"
OUTPUT = BASE / "outputs" / "final_pader_report.txt"

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")


def load_evidence():
    with open(EVIDENCE, encoding="utf-8") as f:
        return json.load(f)


def generate_report():
    data = load_evidence()

    prompt = f"""
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

{json.dumps(data, indent=2, default=str)}
"""

    llm = ChatGroq(
        api_key=API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0
    )

    print("Generating report...")

    response = llm.invoke(prompt)

    return response.content


def save_report(report):
    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    print("Report saved:")
    print(OUTPUT)


if __name__ == "__main__":

    print("Starting PADER report...")

    report = generate_report()

    print("\nFINAL PADER REPORT\n")
    print(report)

    save_report(report)

from pathlib import Path
from docx import Document


BASE = Path(__file__).parent
INPUT = BASE / "outputs/final_pader_report.txt"
OUTPUT = BASE / "outputs/final_pader_report.docx"


def create_report():

    doc = Document()

    text = INPUT.read_text(
        encoding="utf-8"
    )

    for line in text.splitlines():

        if line.strip():
            doc.add_paragraph(line)

    doc.save(OUTPUT)

    print("DOCX created:")
    print(OUTPUT)


if __name__ == "__main__":
    create_report()
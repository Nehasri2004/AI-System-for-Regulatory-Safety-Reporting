from data.load_data import load_data
from data.analysis import analyze_cases
from rag_files.evidence import create_evidence
from generator import generate_report
from generator import save_report


def main():

    print("\n=== AI PADER SAFETY REPORTING ===\n")

    print("1. Loading data...")
    df = load_data()

    print("2. Running analysis...")
    analyze_cases(df)

    print("3. Creating evidence...")
    create_evidence()

    print("4. Generating PADER report...")
    report = generate_report()

    print("5. Saving report...")
    save_report(report)

    print("\nPROJECT COMPLETED!")
    print("Report saved in outputs folder.")


if __name__ == "__main__":
    main()
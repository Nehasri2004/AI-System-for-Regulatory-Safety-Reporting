import json
from pathlib import Path
from data.load_data import load_data


OUT = Path("outputs/analysis.json")


def analyze_cases(df):

    result = {}

    result["total_cases"] = len(df)

    # Serious cases
    if "seriousness" in df.columns:
        result["serious_cases"] = int(
            df["seriousness"].astype(str).str.lower()
            .str.contains("serious").sum()
        )

    # Sex distribution
    if "sex" in df.columns:
        result["sex"] = df["sex"].value_counts().to_dict()

    # Age distribution
    if "age" in df.columns:
        result["age"] = df["age"].value_counts().to_dict()

    # Country distribution
    if "country" in df.columns:
        result["country"] = df["country"].value_counts().to_dict()

    # Outcome
    if "outcome" in df.columns:
        result["outcome"] = df["outcome"].value_counts().to_dict()

    OUT.parent.mkdir(exist_ok=True)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, default=str)

    print("Analysis saved:", OUT)

    return result


if __name__ == "__main__":

    df = load_data()

    result = analyze_cases(df)

    print("\nAnalysis completed!")
    print(result)
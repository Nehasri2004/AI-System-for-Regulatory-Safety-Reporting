import pandas as pd


REQUIRED_COLUMNS = [
    "safetyreportid",
    "patient_patientonsetage",
    "patient_patientsex",
    "occurcountry",
    "patient_reaction_reactionmeddrapt",
    "patient_reaction_reactionoutcome",
    "serious",
    "report_date"
]


def validate_data(df):

    print("\n========== DATA VALIDATION ==========")

    # Check required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        print("Missing columns:")
        for column in missing_columns:
            print("-", column)

        return False

    print("✓ Required columns are present")

    # Check empty dataset
    if df.empty:
        print("✗ Dataset is empty")
        return False

    print("✓ Dataset is not empty")

    # Check safety report IDs
    missing_case_ids = df["safetyreportid"].isna().sum()

    print(
        f"Missing safety report IDs: {missing_case_ids}"
    )

    # Check duplicate rows
    duplicate_rows = df.duplicated().sum()

    print(
        f"Duplicate rows: {duplicate_rows}"
    )

    # Check number of unique cases
    unique_cases = df["safetyreportid"].nunique()

    print(
        f"Unique safety cases: {unique_cases}"
    )

    print("✓ Validation completed")

    return True
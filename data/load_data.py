import pandas as pd
from pathlib import Path


# Location of the Excel dataset
DATA_PATH = Path("C:/Users/nehas/Downloads/Ai regular safety reorting/Bisoprolol_icsr_sample_1068rows.xlsx")


def load_data():
    """
    Load the Bisoprolol safety dataset from Excel.
    """

    # Check whether the file exists
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    # Read Excel file
    df = pd.read_excel("C:/Users/nehas/Downloads/Ai regular safety reorting/Bisoprolol_icsr_sample_1068rows.xlsx")

    # Basic validation
    if df.empty:
        raise ValueError("The dataset is empty.")

    print(f"Dataset loaded successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df


if __name__ == "__main__":
    df = load_data()

    print("\nColumn names:")
    for column in df.columns:
        print(column)

    print("\nFirst 5 rows:")
    print(df.head())
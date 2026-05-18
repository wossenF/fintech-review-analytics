import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


def main():
    root = Path(__file__).resolve().parent.parent
    csv_path = root / "data" / "processed" / "reviews_with_analysis.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {csv_path}")

    df = pd.read_csv(csv_path)

    # allow overriding DB URL via env var for local/CI flexibility
    default_db = "postgresql+psycopg2://postgres:1234@localhost:5432/bank_reviews"
    database_url = os.getenv("DATABASE_URL", default_db)

    engine = create_engine(database_url)

    # Prepare banks dataframe to match DB schema (bank_name, app_name)
    banks = df[["bank"]].drop_duplicates().rename(columns={"bank": "bank_name"})
    banks["app_name"] = banks["bank_name"] + " Mobile App"

    try:
        banks.to_sql("banks", engine, if_exists="append", index=False)
    except Exception as e:
        print("Failed to insert banks table:", e)
        raise

    try:
        banks_db = pd.read_sql("SELECT * FROM banks", engine)
    except Exception as e:
        print("Failed to read banks table from DB:", e)
        raise

    # merge on bank name from CSV with bank_name from DB to obtain bank_id
    df = df.merge(banks_db, left_on="bank", right_on="bank_name")

    # ensure required columns exist (provide sensible defaults when missing)
    if "date" not in df.columns:
        df["date"] = pd.NA
    if "source" not in df.columns:
        df["source"] = "unknown"

    reviews_df = df[[
        "review",
        "rating",
        "date",
        "sentiment",
        "sentiment_score",
        "theme",
        "source",
        "bank_id",
    ]]

    reviews_df = reviews_df.rename(columns={
        "review": "review_text",
        "date": "review_date",
        "sentiment": "sentiment_label",
    })

    try:
        reviews_df.to_sql("reviews", engine, if_exists="append", index=False)
    except Exception as e:
        print("Failed to insert reviews:", e)
        raise


if __name__ == "__main__":
    main()

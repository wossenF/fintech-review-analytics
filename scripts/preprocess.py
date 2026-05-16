import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/raw/reviews_raw.csv")

# -----------------------------
# CLEANING
# -----------------------------

# Remove duplicates
df = df.drop_duplicates(subset=["review"])

# Drop missing values
df = df.dropna(subset=["review", "rating"])

# Normalize date format
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Reset index
df = df.reset_index(drop=True)

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------
df.to_csv("data/cleaned/reviews_clean.csv", index=False)

print("Cleaned dataset size:", len(df))
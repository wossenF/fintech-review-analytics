(This file documents the scripts available in the `scripts/` folder and how to use them.)

Available scripts
- `scrape_reviews.py`
	- Description: Scrapes reviews from Google Play (via `google_play_scraper`) for the apps listed in the `APPS` mapping.
	- Output: `data/raw/reviews_raw.csv` (CSV of raw reviews)
	- Usage:

```bash
python scripts/scrape_reviews.py
```

- `preprocess.py`
	- Description: Loads `data/raw/reviews_raw.csv`, removes duplicates and missing values, normalizes date formats, and writes `data/cleaned/reviews_clean.csv`.
	- Usage:

```bash
python scripts/preprocess.py
```

- `themes.py`
	- Description: Small helper `assign_theme(text)` which assigns a simple theme label to review text using keyword matching. Used by `notebooks/02_sentiment_analysis.ipynb` and related analysis.
	- Notes: The function is deliberately simple and import-safe; consider replacing it with an ML-based classifier if you need higher accuracy.

Tips
- Ensure `data/raw/reviews_raw.csv` exists before running `preprocess.py`.
- Run the scraper from the repository root so the relative paths resolve correctly.


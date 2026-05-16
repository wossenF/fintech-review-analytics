This folder contains Jupyter notebooks used for analysis and visualization. Brief descriptions:

- `01_data_exploration.ipynb`
	- Inspect dataset quality, distributions, rating breakdowns, and common words.

- `02_sentiment_analysis.ipynb`
	- Run a Hugging Face `transformers` sentiment pipeline to classify reviews.
	- Adds `sentiment` and `sentiment_score` columns to the loaded DataFrame.
	- Uses `scripts/themes.py`'s `assign_theme()` helper to label reviews with simple themes.

- `03_theme_analysis.ipynb`
	- Topic and theme extraction (placeholder — expand with LDA or transformer-based clustering if needed).

- `04_visualizations_insights.ipynb`
	- Charts and summary insights for reporting.

Notes
- After running `scripts/scrape_reviews.py` and `scripts/preprocess.py`, open `02_sentiment_analysis.ipynb` to run sentiment inference. The notebook import path was fixed to allow `from themes import assign_theme`.
- If notebooks need to save output CSVs (e.g., `reviews_with_sentiment.csv`), I can add saving cells.

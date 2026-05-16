# fintech-review-analytics

A small pipeline for scraping, cleaning, and analyzing Google Play reviews for Ethiopian banking apps. The project includes scraping scripts, preprocessing, and Jupyter notebooks for exploration, sentiment and theme analysis, and visualizations.

**Project Structure**
- **data/**: Raw and cleaned CSV review datasets.
	- [data/raw/reviews_raw.csv](data/raw/reviews_raw.csv)
	- [data/cleaned/reviews_clean.csv](data/cleaned/reviews_clean.csv)
- **notebooks/**: Analysis and visualizations.
	- [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)
	- [notebooks/02_sentiment_analysis.ipynb](notebooks/02_sentiment_analysis.ipynb)
	- [notebooks/03_theme_analysis.ipynb](notebooks/03_theme_analysis.ipynb)
	- [notebooks/04_visualizations_insights.ipynb](notebooks/04_visualizations_insights.ipynb)
- **scripts/**: Utilities to scrape and preprocess reviews.
	- [scripts/scrape_reviews.py](scripts/scrape_reviews.py)
	- [scripts/preprocess.py](scripts/preprocess.py)
- **src/**: Project code (library modules).
- **tests/**: Tests (if added).

**Quick Start**
1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the scraper (writes raw CSV to `data/raw/reviews_raw.csv`):

```bash
python scripts/scrape_reviews.py
```

3. Preprocess the raw data (writes cleaned CSV to `data/cleaned/reviews_clean.csv`):

```bash
python scripts/preprocess.py
```

4. Open the notebooks in `notebooks/` to explore analyses and visualizations.

**Scripts**
- `scripts/scrape_reviews.py`: Uses `google_play_scraper` to pull up to a configured number of reviews for the apps listed in the `APPS` mapping. Results are saved to [data/raw/reviews_raw.csv](data/raw/reviews_raw.csv).
- `scripts/preprocess.py`: Loads `data/raw/reviews_raw.csv`, removes duplicates/missing values, normalizes dates, and writes [data/cleaned/reviews_clean.csv](data/cleaned/reviews_clean.csv).

**Notebooks** (brief)
- `01_data_exploration.ipynb`: Initial data checks and distributions.
- `02_sentiment_analysis.ipynb`: Sentiment classification experiments and metrics.
- `03_theme_analysis.ipynb`: Topic/theme extraction and qualitative review.
- `04_visualizations_insights.ipynb`: Final charts and insights for reporting.

**Dependencies**
- See [requirements.txt](requirements.txt) for the main Python packages used (pandas, transformers, nltk, scikit-learn, etc.).

**Next steps / Notes**
- Consider adding a `config` file or CLI flags to `scrape_reviews.py` for more flexible scraping (app IDs, country, language, count).
- Add tests under `tests/` and CI workflows for reproducibility.

**Recent updates (delta)**
- Added `scripts/themes.py`: a small, import-safe helper `assign_theme(text)` that assigns a theme label (e.g. "Login Issues", "Performance Issues", "UI/UX") using keyword matching. It is used by the sentiment/theme analysis workflow and can be replaced with a ML-based classifier later.
- Fixed import path in `notebooks/02_sentiment_analysis.ipynb` so notebooks import utilities from the `scripts/` folder correctly.
- Cleaned up `scripts/themes.py` to remove accidental top-level analysis code; the module is now safe to import from notebooks and scripts.

If you'd like, I can also:
- run the notebooks end-to-end and save outputs (e.g., a `reviews_with_sentiment.csv`),
- replace `assign_theme()` with a trained classifier, or
- add CLI flags and configuration for the scraper.

If you want, I can:
- run the scripts to regenerate datasets,
- expand the `scripts/README.md` and `notebooks/README.md`, or
- add a small CLI wrapper for the pipeline.


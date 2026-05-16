from google_play_scraper import reviews, Sort
import pandas as pd
from tqdm import tqdm

# -----------------------------
# CONFIGURATION
# -----------------------------
APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

REVIEWS_PER_APP = 400

# -----------------------------
# SCRAPER FUNCTION
# -----------------------------
def scrape_app(app_id, bank_name):
    all_reviews = []

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        sort=Sort.NEWEST,
        count=REVIEWS_PER_APP
    )

    for r in result:
        all_reviews.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].date(),
            "bank": bank_name,
            "source": "Google Play"
        })

    return all_reviews


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    dataset = []

    for bank, app_id in tqdm(APPS.items()):
        print(f"Scraping {bank}...")
        data = scrape_app(app_id, bank)
        dataset.extend(data)

    df = pd.DataFrame(dataset)

    # Save raw data
    df.to_csv("data/raw/reviews_raw.csv", index=False)

    print("Scraping completed:", len(df))


if __name__ == "__main__":
    main()
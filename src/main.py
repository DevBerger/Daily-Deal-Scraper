from scraper import extract_dispensary_from_url, scrape_todays_specials, scrape_ayr_specials
from csv_writer import write_deals_to_csv

# Generic Dutchie-style dispensaries — scraped with the standard loader
GENERIC_URLS = [
    "https://amplifydispensary.com/stores/amplify-bedford/specials",
]

# Ayr dispensaries — scraped via a visible browser window to bypass Cloudflare.
# Added Ayr Woodmere (ayr-oh-woodmere) on 2026-08-07.
AYR_SLUGS = [
    "ayr-oh-woodmere",
]


def main():
    all_rows = []

    for url in GENERIC_URLS:
        dispensary_name = extract_dispensary_from_url(url)
        deals = scrape_todays_specials(url)
        if not deals:
            print(f"No deals found for {dispensary_name}.")
            continue
        all_rows.extend((dispensary_name, deal) for deal in deals)
        print(f"Found {len(deals)} deals for {dispensary_name}.")

    for slug in AYR_SLUGS:
        deals = scrape_ayr_specials(slug)
        if not deals:
            print(f"No deals found for {slug}.")
            continue
        all_rows.extend((slug, deal) for deal in deals)
        print(f"Found {len(deals)} deals for {slug}.")

    if not all_rows:
        print("No deals found for any dispensary.")
        return

    write_deals_to_csv(all_rows)
    print(f"Exported {len(all_rows)} deals to Desktop/DailyDeals.csv")


if __name__ == "__main__":
    main()
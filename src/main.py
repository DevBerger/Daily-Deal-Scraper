from datetime import datetime
from scraper import extract_dispensary_from_url, scrape_todays_specials
from csv_writer import write_deals_to_csv

URL = "https://amplifydispensary.com/stores/amplify-bedford/specials"


def main():
    dispensary_name = extract_dispensary_from_url(URL)
    deals = scrape_todays_specials(URL)

    if not deals:
        print("No deals found.")
        return

    write_deals_to_csv(deals, dispensary_name)
    print(f"Exported {len(deals)} deals to Desktop/DailyDeals.csv")


if __name__ == "__main__":
    main()
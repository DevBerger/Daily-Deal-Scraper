import re
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Tag
from playwright.sync_api import sync_playwright
import csv
from datetime import date


TODAYS_SPECIALS_PATTERN = re.compile(r"today(?:’|')?s specials", re.IGNORECASE)


def extract_dispensary_from_url(url: str) -> str:
    path_parts = [part for part in urlparse(url).path.split("/") if part]
    return path_parts[1] if len(path_parts) > 1 else ""


def _is_deal_tag(tag: Tag) -> bool:
    text = tag.get_text(strip=True)
    classes = " ".join(tag.get("class", []))
    return bool(text and "Title" in classes)


def _extract_deals_from_container(container: Tag) -> list[str]:
    deals: list[str] = []
    for tag in container.find_all(["p", "span", "h1", "h2", "h3", "h4"]):
        if _is_deal_tag(tag):
            text = tag.get_text(strip=True)
            if text:
                deals.append(text)
    return list(dict.fromkeys(deals))


def _find_todays_specials_container(soup: BeautifulSoup) -> Tag | None:
    heading = soup.find(string=TODAYS_SPECIALS_PATTERN)
    if not heading:
        return None

    container = heading.parent
    for _ in range(6):
        if not container:
            break

        deals = _extract_deals_from_container(container)
        if deals:
            return container

        container = container.parent

    return heading.parent


def scrape_todays_specials(url: str) -> list[str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 2000})
        page.goto(url, wait_until="networkidle", timeout=60000)
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    container = _find_todays_specials_container(soup)

    if container:
        deals = _extract_deals_from_container(container)
        if deals:
            return deals

    return []


def main() -> None:
    url = "https://amplifydispensary.com/stores/amplify-bedford/specials"
    dispensary = extract_dispensary_from_url(url)
    deals = scrape_todays_specials(url)

    rows = [{"dispensary": dispensary, "date": date.today().isoformat(), "deal": d} for d in deals]

    output = "/Users/bradberger/Desktop/DailyDeals.csv"
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["dispensary", "date", "deal"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Found {len(rows)} deals.")
    print(f"Saved to {output}")


if __name__ == "__main__":
    main()
# Daily Deals Scraper — User Instructions

## What It Does
Scrapes today's dispensary deals and saves them to a CSV file on your Desktop (`DailyDeals.csv`).

**Current dispensaries:**
- Amplify Bedford — fully automated (headless)
- Ayr Woodmere — requires a visible browser window (see step 4 below)

---

## How to Run

### 1. Open a terminal and navigate to the project
```bash
cd /Users/bradberger/GIT/daily-deals-scraper
```

### 2. Run the scraper
```bash
python3 src/main.py
```

### 3. Amplify Bedford runs automatically
No action needed — it scrapes in the background.

### 4. Solve the Ayr Cloudflare challenge (if it appears)
A **Chrome window will open** and navigate to the Ayr Woodmere specials page.

- If you see a **"Verifying you are human"** or **"Just a moment…"** page, wait a few seconds — it often auto-resolves.
- If it doesn't resolve on its own, click the checkbox or follow any on-screen prompt.
- Once the deals are visible on screen, the scraper grabs them **automatically** and closes the window. You don't need to do anything else.
- You have **up to 60 seconds** before it times out and uses a cached snapshot instead.

### 5. Check the output
Open `~/Desktop/DailyDeals.csv` — it will contain columns:

| Date | Dispensary | Deal |
|------|------------|------|
| 08/07/26 | amplify-bedford | 20% Off Flower |
| 08/07/26 | ayr-oh-woodmere | 20% Off Store Specific |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `No deals found for amplify-bedford` | Check your internet connection and try again |
| Ayr deals show old/cached data | Cloudflare blocked the live page; the CSV still contains the last known snapshot. Try running again later |
| `ModuleNotFoundError` | Run `pip3 install -r requirements.txt` then try again |
| Chrome window opens and immediately closes | Run again — Cloudflare sometimes resolves on the second attempt |

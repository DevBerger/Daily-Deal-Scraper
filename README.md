# Daily Deals Scraper

This project is designed to scrape the Today's Specials section from the Amplify Dispensary website and save the extracted deals into a CSV file.

## Project Structure

```
daily-deals-scraper
├── src
│   ├── scraper.py       # Contains functions to scrape the specials from the website
│   ├── csv_writer.py    # Includes functions to write the specials to a CSV file
│   └── main.py          # Entry point for the application
├── requirements.txt      # Lists the required Python packages
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd daily-deals-scraper
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the scraper, execute the following command in your terminal:
```
python src/main.py
```

This will scrape the Today's Specials from the specified URL and save the deals to a CSV file named `DailyDeals.csv` on your Desktop.

## Dependencies

This project requires the following Python packages:
- `requests`
- `beautifulsoup4`

Make sure to install these packages using the provided `requirements.txt`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
import csv
import os
from datetime import datetime

def write_deals_to_csv(deals, dispensary_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    csv_file_path = os.path.join(desktop_path, "DailyDeals.csv")
    report_date = datetime.now().strftime("%m/%d/%y")

    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Dispensary", "Deal"])

        for deal in deals:
            writer.writerow([report_date, dispensary_name, deal])
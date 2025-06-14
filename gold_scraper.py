import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

def get_gold_prices():
    try:
        url = "https://www.goodreturns.in/gold-rates/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", class_="gold_silver_table")

        rows = table.find_all("tr")
        gold_22k = gold_24k = None

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                if "22 Carat" in cols[0].text:
                    gold_22k = cols[1].text.strip().replace("₹", "").replace(",", "")
                elif "24 Carat" in cols[0].text:
                    gold_24k = cols[1].text.strip().replace("₹", "").replace(",", "")

        if not gold_22k or not gold_24k:
            raise ValueError("Couldn't find gold prices.")

        return {
            "24k_per_gram": gold_24k,
            "22k_per_gram": gold_22k
        }

    except Exception as e:
        print(f"[ERROR] Could not scrape gold prices: {e}")
        return None

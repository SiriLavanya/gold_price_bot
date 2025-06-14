import requests
from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup

def get_gold_prices():
    try:
        url = "https://www.goodreturns.in/gold-rates/"  # works on Render
        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad status

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", class_="gold_silver_table")  # main gold table

        rows = table.find_all("tr")
        gold_22k = None
        gold_24k = None

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

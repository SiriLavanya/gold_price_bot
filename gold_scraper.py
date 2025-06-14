import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_gold_silver_prices():
    url = "https://www.lalithaajewellery.com/"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.find("a", attrs={"data-toggle": "modal", "data-target": "#price"})

    if price_tag:
        price_text = price_tag.get_text(strip=True)
        prices = price_text.split('|')

        if len(prices) >= 2:
            # Use regex to find the number that directly follows 'Rs.'
            gold_match = re.search(r'Gold 22k[^=]*=\s*Rs\.?\s*(\d+\.?\d*)', prices[0])
            silver_match = re.search(r'Silver[^=]*=\s*Rs\.?\s*(\d+\.?\d*)', prices[1])

            if gold_match and silver_match:
                gold_price_22k = float(gold_match.group(1))
                silver_price = float(silver_match.group(1))
                gold_price_24k = round(gold_price_22k * 1.09, 2)

                return {
                    "date": datetime.today().strftime("%d-%m-%Y"),
                    "gold_22k_1g": gold_price_22k,
                    "gold_22k_10g": round(gold_price_22k * 10, 2),
                    "gold_24k_1g": gold_price_24k,
                    "gold_24k_10g": round(gold_price_24k * 10, 2),
                    "silver_1g": silver_price,
                    "silver_10g": round(silver_price * 10, 2)
                }
            else:
                print("⚠️ Regex did not match the expected Rs. values.")
        else:
            print("⚠️ Prices not split correctly. Check website format.")
    else:
        print("❌ Price tag not found.")
    return None

def format_price_message(prices):
    return (
        f"🌟 Hello! Gold Price Update for {prices['date']}:\n"
        f"💛 24K Gold: ₹{prices['gold_24k_1g']}/gm | ₹{prices['gold_24k_10g']}/10gm\n"
        f"💫 22K Gold: ₹{prices['gold_22k_1g']}/gm | ₹{prices['gold_22k_10g']}/10gm\n"
        f"🥈 Silver: ₹{prices['silver_1g']}/gm | ₹{prices['silver_10g']}/10gm"
    )

if __name__ == "__main__":
    prices = get_gold_silver_prices()
    if prices:
        print(format_price_message(prices))
    else:
        print("❌ Failed to fetch gold and silver prices.")

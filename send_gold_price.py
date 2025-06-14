from gold_scraper import get_gold_prices
from whatsapp_sender import send_whatsapp_message

def main():
    prices = get_gold_prices()
    if prices:
        send_whatsapp_message(prices['22k_per_gram'], prices['24k_per_gram'])
    else:
        print("[ERROR] Could not fetch gold prices.")

if __name__ == "__main__":
    main()

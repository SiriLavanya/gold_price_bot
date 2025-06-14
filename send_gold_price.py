from gold_scraper import get_gold_silver_prices
from whatsapp_sender import send_whatsapp_message

def format_message(data):
    return f"""🌟 Hello! Gold Price Update for {data['date']}:
💛 24K Gold: ₹{data['gold_24k_1g']}/gm | ₹{data['gold_24k_10g']}/10gm
💫 22K Gold: ₹{data['gold_22k_1g']}/gm | ₹{data['gold_22k_10g']}/10gm
🥈 Silver: ₹{data['silver_1g']}/gm | ₹{data['silver_10g']}/10gm"""

def main():
    data = get_gold_silver_prices()
    if data:
        message = format_message(data)
        print("🔍 Preview:\n" + message)
        send_whatsapp_message(data)  # data dictionary will be passed to whatsapp_sender

if __name__ == "__main__":
    main()

import os
from twilio.rest import Client
from dotenv import load_dotenv
import datetime

# Load environment variables from .env file
load_dotenv()

# Twilio credentials
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919390673042'  # ✅ You can update this dynamically if needed

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(data):
    """
    Sends a WhatsApp message with gold & silver price updates.
    :param data: Dictionary containing price data with keys:
                 gold_22k_1g, gold_22k_10g, gold_24k_1g, gold_24k_10g, silver_1g, silver_10g, date
    """
    message_body = (
        f"🌟 Hello! Gold Price Update for {data['date']}:\n"
        f"💛 24K Gold: ₹{data['gold_24k_1g']}/gm | ₹{data['gold_24k_10g']}/10gm\n"
        f"💫 22K Gold: ₹{data['gold_22k_1g']}/gm | ₹{data['gold_22k_10g']}/10gm\n"
        f"🥈 Silver: ₹{data['silver_1g']}/gm | ₹{data['silver_10g']}/10gm"
    )

    message = client.messages.create(
        from_=from_whatsapp_number,
        body=message_body,
        to=to_whatsapp_number
    )

    print(f"[✅] WhatsApp message sent! SID: {message.sid}")

import os
from twilio.rest import Client
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Twilio credentials from .env
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919390673042'

# Create Twilio client
client = Client(account_sid, auth_token)

def send_whatsapp_message(gold_22k, gold_24k):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    message_body = (
        f"💰 *Gold Price Update ({now})* 💰\n"
        f"👉 22K per gram: ₹{gold_22k}\n"
        f"👉 24K per gram: ₹{gold_24k}"
    )

    message = client.messages.create(
        from_=from_whatsapp_number,
        body=message_body,
        to=to_whatsapp_number
    )

    print(f"[INFO] Message sent successfully! SID: {message.sid}")

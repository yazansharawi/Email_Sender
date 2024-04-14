from twilio.rest import Client
import config

ACCOUNT_SID = config.ACCOUNT_SID
AUTH_TOKEN = config.AUTH_TOKEN


def send_whatsapp_message(recipient_number, message_text):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_text,
        to=recipient_number
    )

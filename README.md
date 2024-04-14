# Email and WhatsApp Automation Project

This project automates sending emails and follow-ups based on data stored in a Google Sheet.  Additionally, it sends WhatsApp notifications upon successful email delivery.

# Project Structure

**main.py:** The main script that handles the logic of fetching data from the Google Sheet, preparing and sending emails, and triggering WhatsApp notifications.

**utilities:**  A folder containing helper modules:

**email_utils.py:** Functions for crafting and sending emails.
whatsapp_utils.py: Functions for sending WhatsApp messages using the Twilio API.

**templates:** Contains the HTML email templates (main-email.html, follow-up-1.html, etc.).

**files:** Contains attachments (e.g., catalog.pdf) to be included in emails.

**config.py:** Stores sensitive information like API keys, email addresses, and WhatsApp numbers.

**google_sheets_credentials.json:** Credentials file for accessing the Google Sheet.



# Email and WhatsApp Automation Project
This project automates sending emails and follow-ups based on data stored in a Google Sheet.  Additionally, it sends WhatsApp notifications upon successful email delivery.

# Project Structure
main.py: The main script that handles the logic of fetching data from the Google Sheet, preparing and sending emails, and triggering WhatsApp notifications.

utilities:  A folder containing helper modules:

email_utils.py: Functions for crafting and sending emails.
whatsapp_utils.py: Functions for sending WhatsApp messages using the Twilio API.
templates: Contains the HTML email templates (main-email.html, follow-up-1.html, etc.).

files: Contains attachments (e.g., catalog.pdf) to be included in emails.

config.py: Stores sensitive information like API keys, email addresses, and WhatsApp numbers.

google_sheets_credentials.json: Credentials file for accessing the Google Sheet.

Setup
Install Dependencies:

Bash
pip install gspread oauth2client twilio jinja2
Use code with caution.
Obtain API Keys:

Create a Google Sheets API project and download the credentials JSON file (google_sheets_credentials.json).
Set up a Twilio account and obtain your Account SID and Auth Token.
Configure config.py:  Create a config.py file with variables like:

Python
SHEET_KEY = "your_google_sheet_key" 
ACCOUNT_SID = "your_twilio_account_sid"
AUTH_TOKEN = "your_twilio_auth_token"

# ... other email or WhatsApp related configuration
Use code with caution.
Google Sheet Setup:

Create a Google Sheet with columns like "Name", "Email", "Status", "Follow-up-1", etc.
Usage
Activate Virtual Environment (optional but recommended):

Bash
source venv/bin/activate 
Use code with caution.
Run the Script:

Bash
python main.py 
Use code with caution.
Cron Job (For Automation)
Set up a cron job to execute main.py at your desired intervals (e.g., every 5 minutes).
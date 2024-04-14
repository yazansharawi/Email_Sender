import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config
from utilities.email_utils import send_email
from utilities.whatsapp_utils import send_whatsapp_message
import logging

logging.basicConfig(filename='/Users/yazansharawi/Desktop/email_sender/main_execution.log', level=logging.INFO) 
logging.info('Started main.py execution')

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_credentials.json', scope)
gspread_client = gspread.authorize(creds)
sheet = gspread_client.open_by_key(config.SHEET_KEY).sheet1
data = sheet.get_all_records()

WHATSAPP_RECIPIENT_NUMBER = config.WHATSAPP_RECIPIENT_NUMBER

email_count = 0
for index, person in enumerate(data, start=2):
    name = person['Name']
    email = person['Email']
    attachment_path = 'files/catalog.pdf' 
    background = "[brief background/experience]"
    attachment_type = "resume/sales portfolio [choose one]"
    current_status = person.get('Status', 'Not Sent')

    try:
        if current_status == 'Not Sent':
            template_file = 'main-email.html'
        elif current_status == 'Sent':
            template_file = 'follow-up-1.html'
            sheet.update_cell(index, 4, "Sent") 
        elif current_status == 'Follow-up-1':
            template_file = 'follow-up-2.html'
            sheet.update_cell(index, 5, "Sent")
        else:
            template_file = None

        if template_file:
            send_email(name, email, attachment_path, background, attachment_type, template_file)
            sheet.update_cell(index, 3, "Sent") 
            email_count += 1
            message_text = f"Email sent to {name} ({email}) with {template_file}"
            send_whatsapp_message(WHATSAPP_RECIPIENT_NUMBER, message_text)

    except Exception as e:
        if current_status == 'Sent':
            sheet.update_cell(index, 4, "Follow-up-1") 
        elif current_status == 'Follow-up-1':
            sheet.update_cell(index, 5, "Follow-up-2") 
        else:
            sheet.update_cell(index, 3, "Not Sent")

        print(f"Error sending email to {email}: {str(e)}")

print(email_count, "emails sent successfully")
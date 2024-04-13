import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config
from email_utils import send_email

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_credentials.json', scope)
gspread_client = gspread.authorize(creds)
sheet = gspread_client.open_by_key(config.SHEET_KEY).sheet1
data = sheet.get_all_records()

email_count = 0
for index, person in enumerate(data, start=2):
    name = person['Name']
    email = person['Email']
    attachment_path = 'files/catalog.pdf'
    background = "[brief background/experience]"
    attachment_type = "resume/sales portfolio [choose one]"
    
    try:
        send_email(name, email, attachment_path, background, attachment_type)
        sheet.update_cell(index, 3, "Sent") 
        email_count += 1
    except Exception as e:
        sheet.update_cell(index, 3, "Not Sent")
        print(f"Error sending email to {email}: {str(e)}")

print(email_count, "emails sent successfully")
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config
from utilities.email_utils import send_email


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google_sheets_credentials.json', scope)
gspread_client = gspread.authorize(creds)
sheet = gspread_client.open_by_key(config.SHEET_KEY).sheet1
data = sheet.get_all_records()


email_count = 0
for person in data:
    name = person['Name']
    email = person['Email']
    bio = person['Bio']
    send_email(name, email) 
    email_count += 1

print(email_count, "emails sent successfully") 

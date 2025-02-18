import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define the API scope
SCOPE = ["https://spreadsheets.google.com/feeds", 
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# Path to the service account JSON key file
CREDENTIALS_FILE = 'rapid-pivot-374815-7815e0456d5b.json'

# Authenticate using the service account credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
client = gspread.authorize(credentials)

# Open the Google Sheet by its name or ID
spreadsheet = client.open_by_key("1moYMGh4g9saysbtBp8wuCgTg6uDm7sJoobWVhzoWBVs")  # Use .open_by_key('your_sheet_id') for the sheet ID
worksheet = spreadsheet.sheet1  # Select the first sheet (Sheet1)

# Function to send data to Google Sheet
def send_data(data):
    # Append the data to the next available row
    concatedArray = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] + data
    worksheet.append_row(concatedArray)

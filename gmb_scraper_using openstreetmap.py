import json
import time
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets credentials and sheet details
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('json_key_file.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('GMB_Scrap_Data').sheet1

# headers to the Google Sheet
sheet.update_cell(1, 1, 'Name')
sheet.update_cell(1, 2, 'Address')

base_url = "https://nominatim.openstreetmap.org/search?format=json&city=Pune&amenity="
amenity_tags = ["shop", "store", "mall",  "pharmacy", "restaurant", "cafe", "furniture", "business"]

for tag in amenity_tags:
    url = base_url + tag
    response = requests.get(url)
    data = response.json()
    for item in data:
        
        sheet.append_row([item['name'], item['display_name']])
        time.sleep(1)  # delay to avoid overwhelming the API

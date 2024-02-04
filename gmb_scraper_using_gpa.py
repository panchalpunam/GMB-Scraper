import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google API key
API_KEY = 'AIzaSyAIIhsvreXsj_jxVSDvsReTlwZQPwGD_GM'

# base URL for the Google Places API
PLACES_API_BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# parameters for your search 
LOCATION = 'Pune'
RADIUS = '50'
KEYWORD = 'Furniture Shop'

# scope for accessing Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Authenticate with Google Sheets using credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('json_key_file.json', scope)
gc = gspread.authorize(credentials)

# Opening google sheet for writing
#sheet = gc.open('GMB_Scrap_Data').sheet1
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1hpn0ZqTWzMafzNRJDkCtcTu9c4bUP-Twd8MXFN1WHU8/edit#gid=0').sheet1


# function to fetch business details from the Google Places API
def fetch_business_details():
    params = {
        'location': LOCATION,
        'radius': RADIUS,
        'keyword': KEYWORD,
        'key': API_KEY
    }
    
    response = requests.get(PLACES_API_BASE_URL, params=params)
    
    data = response.json()
    print(data)
    if 'results' in data:
        for result in data['results']:
            name = result.get('name', '')
            address = result.get('vicinity', '')
            # Add more details as needed (e.g., phone number, website, etc.)
            
            # Write the details to the Google Sheet
            sheet.append_row([name, address])
    else:
        print('No results found.')


if __name__ == "__main__":
    fetch_business_details()

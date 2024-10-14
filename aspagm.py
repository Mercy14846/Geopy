import requests
import pandas as pd

# Google Maps API Key (replace 'YOUR_API_KEY' with your actual key)
API_KEY = 'API_KEY'

# Function to get address using Google Maps Geocoding API
def get_address_from_google_maps(lat, lon, api_key=API_KEY):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={api_key}&language=en"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if len(result['results']) > 0:
            return result['results'][0]['formatted_address']
        else:
            return "Address not found"
    else:
        return "Error: " + str(response.status_code)

# Load the CSV file (replace with your actual file path)
df = pd.read_csv('not_found.csv')

# Add the address column using Google Maps API
df['Address'] = df.apply(lambda row: get_address_from_google_maps(row['lat'], row['lon']), axis=1)

# Save the updated CSV file
df.to_csv('updated_file.csv', index=False)

print("Addresses added and CSV file updated.")

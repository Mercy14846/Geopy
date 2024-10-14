import pandas as pd
import requests
import time

# Function to get address using Nominatim API (OSM)
def get_address_from_osm(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1&accept-language=en"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if 'address' in result:
            address = result['display_name']
            return address
        else:
            return "Address not found"
    else:
        return f"Error: {response.status_code}"

# Load the CSV file (replace with your actual file path)
file_path = 'aspa.csv'
df = pd.read_csv(file_path)

# Add the address column using OSM (Nominatim)
df['Address'] = df.apply(lambda row: get_address_from_osm(row['lat'], row['lon']), axis=1)

# Save the updated CSV file
output_file_path = 'aspa_with_osm_addresses.csv'
df.to_csv(output_file_path, index=False)

output_file_path

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Set up retries with backoff
retry_strategy = Retry(
    total=3,
    backoff_factor=1,  # Wait 1 second between retries
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

def get_address_from_osm(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1&accept-language=en"
    try:
        response = http.get(url)
        if response.status_code == 200:
            result = response.json()
            if 'address' in result:
                return result['display_name']
            else:
                return "Address not found"
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.SSLError as e:
        return f"SSL Error: {e}"

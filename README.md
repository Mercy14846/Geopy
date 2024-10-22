# Reverse Geocoding with OpenStreetMap (OSM) and Python
This project demonstrates how to use the OpenStreetMap Nominatim API to perform reverse geocoding, converting latitude and longitude coordinates into human-readable addresses, and update a CSV file with this information.

## Features
- Takes a CSV file containing `lat` and `lon` coordinates.
- Uses the Nominatim API to fetch addresses for each coordinate pair.
- Updates the CSV file by adding the corresponding address in English.
- Handles errors such as network issues or SSL failures.

## Requirements
- Python 3.x
- The following Python libraries:
- - `requests`
- - `pandas`

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
```
2. Install the required dependencies:
```bash
pip install pandas requests
```

## How to Use
1. Prepare your CSV file: Ensure your CSV file has at least the following columns:
- `lat` (latitude)
- `lon` (longitude)
  
Example CSV:
<!-- prettier-ignore-start -->
| ID | lat | lon	| Address |
|----|-----|------|---------|
| MLM00061233 | 15.167 | -7.283 | NaN |
| SF000225210	| 33.680 | 19.320	| NaN |
<!-- prettier-ignore-end -->

2. Run the Script:
Replace the path to your CSV file in the script and run it:
```bash
python reverse_geocode_osm.py
```
The script will fetch addresses using the OSM Nominatim API and update your CSV file with the results.

3. Handling Errors: If you encounter an SSL error or network issue, the script retries the request up to 3 times with a delay.

4. Output: The script will save the updated CSV file with the fetched addresses.

## Example Code
python
```python
import pandas as pd
import requests
import time

# Function to get address using Nominatim API (OSM)
def get_address_from_osm(lat, lon):
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1&accept-language=en"
    try:
        response = requests.get(url)
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

# Load the CSV file
df = pd.read_csv('your_file.csv')

# Add the address column using OSM (Nominatim)
df['Address'] = df.apply(lambda row: get_address_from_osm(row['lat'], row['lon']), axis=1)

# Save the updated CSV file
df.to_csv('updated_file.csv', index=False)
```

## Troubleshooting
*SSL Errors*
If you encounter SSL errors, you can switch to using HTTP instead of HTTPS, or add retries to the requests with a delay.

## Rate Limiting
The Nominatim API has rate limits. To avoid hitting those limits, add a `time.sleep(1)` to pause between requests.

## License
This project is licensed under the [MIT License] - see the (LICENSE) file for details.

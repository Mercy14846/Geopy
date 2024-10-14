import pandas as pd

# Load the CSV file
file_path = 'not_found.csv'
df = pd.read_csv(file_path)

# Preview the CSV file to understand its structure
df.head(5)

from geopy.geocoders import Nominatim

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get address from latitude and longitude
def get_address(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), timeout=50)
        return location.address if location else "Address not found"
    except:
        return "Error fetching address"

# Apply the function to each row and add it to the Address column
df['Address'] = df.apply(lambda row: get_address(row['lat'], row['lon']), axis=1)

# Display the updated dataframe
df.head()

# Save the updated CSV with the addresses
output_file_path = 'not_found.csv'
df.to_csv(output_file_path, index=False)

output_file_path



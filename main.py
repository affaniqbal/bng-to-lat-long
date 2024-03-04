import pandas as pd
import requests

#ensure the columns are labelled as 'eastings' and 'northings'. If they are named differently, edit code in line 9.
df = pd.read_csv("YOUR-CSV-FILE-HERE")

# Function to convert eastings and northings to latitude and longitude using a URL
def convert_to_latitude_longitude(row):
    url = f"http://webapps.bgs.ac.uk/data/webservices/CoordConvert_LL_BNG.cfc?method=BNGtoLatLng&easting={row['eastings']}&northing={row['northings']}"
    
    # Make the GET request
    response = requests.get(url)
    
    # Parse the JSON response directly
    data = response.json()
    
    return data.get("LATITUDE"), data.get("LONGITUDE")

# Apply the function to create new columns
df[['latitude', 'longitude']] = df.apply(convert_to_latitude_longitude, axis=1, result_type='expand')

# Save the updated DataFrame to the original CSV
df.to_csv("SPECIFY-NEW-CSV-FILE-NAME-HERE", index=False)

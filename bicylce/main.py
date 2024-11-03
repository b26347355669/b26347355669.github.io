import requests
import json

# LTA API Details
url = "https://datamall2.mytransport.sg/ltaodataservice/BicycleParkingv2"
headers = {
    "AccountKey": "U51f2z/HTiuLI0DeYuJ8HA==",  # Replace with your LTA API key
    "accept": "application/json"
}

# Helper function to generate float ranges


def frange(start, stop, step):
    while start < stop:
        yield round(start, 5)  # Round to avoid floating-point precision issues
        start += step


# Define grid covering Singapore's area
lat_start, lat_end = 1.22, 1.47
long_start, long_end = 103.6, 104.0
step = 0.01  # Approximately 1.1 km per step

# Generate grid points
grid_points = [(lat, lon) for lat in frange(lat_start, lat_end, step)
               for lon in frange(long_start, long_end, step)]

# Fetch bicycle parking data and deduplicate entries


def fetch_bicycle_parking_data(latitude, longitude, radius=0.5):
    params = {
        "Lat": latitude,
        "Long": longitude,
        "Dist": radius
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()["value"]
    return data


# Collect data with deduplication
all_bicycle_parking = {}
for lat, lon in grid_points:
    data = fetch_bicycle_parking_data(lat, lon)
    for location in data:
        key = (location["Latitude"], location["Longitude"])
        if key not in all_bicycle_parking:
            all_bicycle_parking[key] = location

# Convert dictionary to list for JSON export
deduplicated_bicycle_parking = list(all_bicycle_parking.values())

# Save data to JSON file for use with Google Maps
with open("bicycle_parking_data.json", "w") as f:
    json.dump(deduplicated_bicycle_parking, f)

print("Data collection complete. Saved deduplicated data to bicycle_parking_data.json.")

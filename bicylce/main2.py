import json
from geopy.distance import geodesic

# Load bicycle parking data
with open("bicycle_parking_data.json", "r") as f:
    data = json.load(f)

# Function to filter racks within a 20-meter threshold


def filter_nearby_racks(racks, threshold=20):
    filtered_racks = []
    for rack in racks:
        # Extract latitude and longitude of current rack
        rack_location = (rack["Latitude"], rack["Longitude"])

        # Check if this rack is at least 'threshold' meters away from all racks in filtered_racks
        if all(geodesic(rack_location, (filtered_rack["Latitude"], filtered_rack["Longitude"])).meters > threshold
               for filtered_rack in filtered_racks):
            # Add rack if no nearby rack is within threshold
            filtered_racks.append(rack)

    return filtered_racks


# Filter racks within 20 meters of each other
filtered_data = filter_nearby_racks(data, threshold=20)

# Save filtered data to a new JSON file
with open("filtered_bicycle_parking_data.json", "w") as f:
    json.dump(filtered_data, f)

print("Filtered data saved to filtered_bicycle_parking_data.json.")

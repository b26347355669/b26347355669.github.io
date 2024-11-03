import json
from scipy.spatial import KDTree

# Load bicycle parking data
with open("bicycle_parking_data_test2.json", "r") as f:
    data = json.load(f)

# Extract coordinates and create KD-tree for fast spatial searching
coordinates = [(rack["Latitude"], rack["Longitude"]) for rack in data]
tree = KDTree(coordinates)

# Set the threshold distance in degrees (approximate, as 20 meters is roughly 0.00018 degrees)
# This approximation works reasonably well for small distances
distance_threshold = 20 / 111320  # Convert 20 meters to degrees

# Track indexes of racks to keep
to_keep = set()

for i, coord in enumerate(coordinates):
    # Query nearby points within the threshold, including itself
    nearby_points = tree.query_ball_point(coord, distance_threshold)

    # Only add the current rack if it’s the first one in the group within 20 meters
    if all(neighbor >= i for neighbor in nearby_points):
        to_keep.add(i)

# Filter original data to keep only the selected racks
filtered_data = [data[i] for i in to_keep]

# Save filtered data to a new JSON file
with open("filtered_bicycle_parking_data2.json", "w") as f:
    json.dump(filtered_data, f)

print("Filtered data saved to filtered_bicycle_parking_data.json.")

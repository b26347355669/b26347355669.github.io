import json

# Load the original geohashes data
with open("decoded_geohashes.json", "r") as original_file:
    original_geohashes = json.load(original_file)

# Load the eliminated geohashes data
with open("decoded_el_geohashes2.json", "r") as eliminated_file:
    eliminated_geohashes = json.load(eliminated_file)

# Create a set of geohashes to eliminate for quick lookup
eliminated_geohash_set = {gh["geohash"] for gh in eliminated_geohashes}

# Filter out eliminated geohashes from the original data
filtered_geohashes = [
    gh for gh in original_geohashes if gh["geohash"] not in eliminated_geohash_set]

# Save the filtered geohashes to a new JSON file
with open("filtered_geohashes2.json", "w") as filtered_file:
    json.dump(filtered_geohashes, filtered_file, indent=4)

print("Filtered geohashes saved to 'filtered_geohashes2.json'")

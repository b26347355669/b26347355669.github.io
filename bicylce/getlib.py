import requests
import json
import time

# Google Maps Geocoding API URL
GEOCODING_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"

# Google Maps API Key
API_KEY = "AIzaSyDLQ7zerFAyUEa0YzusDYSbGcTfVOMi_O8"  # Replace with your API key

# List of libraries and their addresses
libraries = [
    {"name": "National Library / Lee Kong Chian Reference Library",
        "address": "100 Victoria Street, Singapore 188064"},
    {"name": "National Archives of Singapore",
        "address": "1 Canning Rise, Singapore 179868"},
    {"name": "The LLiBrary",
        "address": "11 Eunos Road 8, #03-02 (Via Lobby B), Singapore 408601"},
    {"name": "Singapore Botanic Gardens’ Library",
        "address": "1 Cluny Rd, Level 1, Botany Centre, Tanglin Entrance, Singapore Botanic Gardens, Singapore 259569"},
    {"name": "Ang Mo Kio Public Library",
        "address": "4300 Ang Mo Kio Avenue 6, Singapore 569842"},
    {"name": "Bedok Public Library",
        "address": "11 Bedok North Street 1, #02-03 & #03-04, Singapore 469662"},
    {"name": "Bishan Public Library",
        "address": "5 Bishan Place, #01-01, Singapore 579841"},
    {"name": "Bukit Batok Public Library",
        "address": "1 Bukit Batok Central Link, #03-01, Singapore 658713"},
    {"name": "Bukit Panjang Public Library",
        "address": "1 Jelebu Road, #04-04 & 16/17, Singapore 677743"},
    {"name": "Central Public Library",
        "address": "100 Victoria Street, Singapore 188064"},
    {"name": "Cheng San Public Library",
        "address": "90 Hougang Avenue 10, #03-11, Singapore 538766"},
    {"name": "Choa Chu Kang Public Library",
        "address": "21 Choa Chu Kang Ave 4, #04-01/02 and #05-06, Singapore 689812"},
    {"name": "Clementi Public Library",
        "address": "3155 Commonwealth Avenue West, #05-13/14/15, Singapore 129588"},
    {"name": "Geylang East Public Library",
        "address": "50 Geylang East Ave 1, Singapore 389777"},
    {"name": "Jurong Regional Library",
        "address": "21 Jurong East Central 1, Singapore 609732"},
    {"name": "Jurong West Public Library",
        "address": "60 Jurong West Central 3, #01-03, Singapore 648346"},
    {"name": "library@chinatown",
        "address": "133 New Bridge Road, #04-12, Singapore 059413"},
    {"name": "library@esplanade", "address": "8 Raffles Avenue, #03-01, Singapore 039802"},
    {"name": "library@harbourfront",
        "address": "1 Harbourfront Walk, #03-05 (Lobby F), Singapore 098585"},
    {"name": "library@orchard",
        "address": "277 Orchard Road, #03-12 / #04-11, Singapore 238858"},
    {"name": "Marine Parade Public Library",
        "address": "278 Marine Parade Road, #01-02, Singapore 449282"},
    {"name": "Pasir Ris Public Library",
        "address": "1 Pasir Ris Central St 3, #04-01/06, Singapore 518457"},
    {"name": "Punggol Regional Library",
        "address": "1 Punggol Drive, #01-12, Singapore 828629"},
    {"name": "Queenstown Public Library",
        "address": "53 Margaret Drive, Singapore 149297"},
    {"name": "Sembawang Public Library",
        "address": "30 Sembawang Drive, #05-01, Singapore 757713"},
    {"name": "Sengkang Public Library",
        "address": "1 Sengkang Square, #03-28 & #04-19, Singapore 545078"},
    {"name": "Serangoon Public Library",
        "address": "23 Serangoon Central, #04-82/83, Singapore 556083"},
    {"name": "Tampines Regional Library",
        "address": "1 Tampines Walk, #02-01, Singapore 528523"},
    {"name": "Toa Payoh Public Library",
        "address": "6 Toa Payoh Central, Singapore 319191"},
    {"name": "Woodlands Regional Library",
        "address": "900 South Woodlands Drive, #01-03, Singapore 730900"},
    {"name": "Yishun Public Library",
        "address": "930 Yishun Ave 2, #04-01, Singapore 769098"}
]

# Function to get latitude and longitude for an address


def geocode_address(address):
    params = {
        "address": address,
        "key": API_KEY
    }
    response = requests.get(GEOCODING_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            print(f"Geocoding error for {address}: {data['status']}")
            return None, None
    else:
        print(f"HTTP error: {response.status_code}")
        return None, None


# Geocode each library and save to JSON
geocoded_libraries = []
for library in libraries:
    lat, lng = geocode_address(library["address"])
    if lat is not None and lng is not None:
        geocoded_library = {
            "name": library["name"],
            "address": library["address"],
            "latitude": lat,
            "longitude": lng
        }
        geocoded_libraries.append(geocoded_library)
        print(f"Geocoded {library['name']}: {lat}, {lng}")
    time.sleep(0.1)  # Delay to avoid hitting API rate limits

# Save the geocoded data to libraries.json
with open("libraries.json", "w") as f:
    json.dump(geocoded_libraries, f, indent=4)

print("Geocoding complete. Data saved to libraries.json.")

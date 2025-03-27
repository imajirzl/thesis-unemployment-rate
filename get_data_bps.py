import os
import requests
import json

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Check if API_KEY is available
if not api_key:
    raise ValueError("API_KEY environment variable not set.")

# API URL
url = f"https://webapi.bps.go.id/v1/api/list/model/data/lang/eng/domain/0000/var/543/key/{api_key}"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to dictionary

    # Save as JSON file
    with open("data_ind.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print("✅ Data saved as data.json")

else:
    print(f"❌ Failed to fetch data: {response.status_code}")

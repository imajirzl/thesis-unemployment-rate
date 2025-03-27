import requests
import json

# API URL with JSON format
url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_UNE_M,1.0/USA+DEU..._Z.N._T.Y_GE15..M?startPeriod=1995-01&endPeriod=2024-12&dimensionAtObservation=AllDimensions&format=jsondata"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to dictionary

    # Save as JSON file
    with open("data_oecd.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print("Data saved as data_oecd.json")

else:
    print(f"Failed to fetch data: {response.status_code}")

import os
import requests
import pandas as pd

# Fetch API key
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set.")

# Fetch data
url = f"https://webapi.bps.go.id/v1/api/list/model/data/lang/eng/domain/0000/var/698/key/{api_key}"
response = requests.get(url)
if response.status_code != 200:
    raise RuntimeError(f"Failed to fetch data: {response.status_code}")

data = response.json()

print(data)

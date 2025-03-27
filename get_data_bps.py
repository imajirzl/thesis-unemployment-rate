import os
import requests
import pandas as pd

# Fetch API key
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set.")

# Fetch data
url = f"https://webapi.bps.go.id/v1/api/list/model/data/lang/eng/domain/0000/var/543/key/{api_key}"
response = requests.get(url)
if response.status_code != 200:
    raise RuntimeError(f"Failed to fetch data: {response.status_code}")

data = response.json()

# Extract Indonesia data (key starts with '9999')
data_ind = {key: value for key, value in data["datacontent"].items() if key.startswith("9999")}

# Process data
records = [
    [1900 + int(key[-5:-3]) if int(key[-5:-3]) > 50 else 2000 + int(key[-5:-3]), 
     {"91": "-", "89": "Q1", "90": "Q3"}.get(key[-2:], None), 
     value] 
    for key, value in data_ind.items() 
]

# Save to CSV
df = pd.DataFrame(records, columns=["Year", "Quarter", "Unemployment_Rate"])
df.to_csv("data_ind.csv", index=False)
print(df)

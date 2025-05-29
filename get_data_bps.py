import os
import requests
import pandas as pd

'''
This script fetches the general unemployment data from the BPS API, processes it, and saves it to a CSV file.
'''

# fetching API key from environment variable
api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY environment variable not set.")

# defining URL for general unemployment rate from BPS API
url = f"https://webapi.bps.go.id/v1/api/list/model/data/lang/eng/domain/0000/var/543/key/{api_key}"
response = requests.get(url)
# checking if the request was successful
if response.status_code != 200:
    raise RuntimeError(f"Failed to fetch data: {response.status_code}")

# parsing the JSON response
data = response.json()

# Extracting only Indonesia data (key starts with '9999'). Note: the data includes province-level unemployment rate as well. 
data_ind = {key: value for key, value in data["datacontent"].items() if key.startswith("9999")}

# Processing each data point into a list of [Year, Quarter, Unemployment_Rate]
records = [
    [1900 + int(key[-5:-3]) if int(key[-5:-3]) > 50 else 2000 + int(key[-5:-3]), # convert two-digit year to four-digit year
     {"91": "-", "89": "Q1", "90": "Q3"}.get(key[-2:], None), # map last two digits to quarter
     value] # actual unemployment rate value
    for key, value in data_ind.items() 
]

# converting records to a dataframe
df = pd.DataFrame(records, columns=["Year", "Quarter", "Unemployment_Rate"])
# saving the dataframe to a CSV file
df.to_csv("data_ind.csv", index=False)
# preview of dataframe
print(df)

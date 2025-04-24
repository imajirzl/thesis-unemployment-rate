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

# mappings
age_group = {1, 2, 3} # youth = 15-19, 20-24, 25-29
year_map = {item['val']: item['label'] for item in data['tahun']}
month_map = {item['val']: item['label'] for item in data['turtahun']}
var_map = {item['val']: item['label'] for item in data['turvar']}
label_to_var_id = {v: k for k, v in var_map.items()}
unemployment_id = label_to_var_id['Total Unemployment']
labor_force_id = label_to_var_id['Total Labor Force']

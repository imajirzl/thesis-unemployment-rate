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
age_map = {1: '15-19', 2: '20-24', 3: '25-29'} # youth 
year_map = {item['val']: item['label'] for item in data['tahun']}
month_map = {item['val']: item['label'] for item in data['turtahun']}
var_map = {item['val']: item['label'] for item in data['turvar']}
label_to_var_id = {v: k for k, v in var_map.items()}
unemployment_id = label_to_var_id['Total Unemployment']
labor_force_id = label_to_var_id['Total Labor Force']

# parse data
records = []
for key, value in data['datacontent'].items():
    key = str(key)
    
    age_id = int(key[0])
    #dataset_id = int(key[1:4])
    var_id = int(key[4:7])
    year_id = int(key[7:10])
    month_id = int(key[10:13])

    if age_id in age_map and var_id in [unemployment_id, labor_force_id]:
        records.append({
            'year': year_map.get(year_id),
            'month': month_map.get(month_id),
            'age_group': age_map.get(age_id),
            'var': var_map.get(var_id),
            'value': value
        })

df = pd.DataFrame(records)
print(df)
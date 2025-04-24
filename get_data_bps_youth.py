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

# pivot to wide format = one column per age group and variable
df_wide = df.pivot_table(index=['year', 'month', 'var'], columns='age_group', values='value').reset_index()
# sum total across age groups
df_wide['Total'] = df_wide[['15-19', '20-24', '25-29']].sum(axis=1)
# pivot to get total unemployment and labor force in columns
df_combined = df_wide.pivot(index=['year', 'month'], columns='var', values='Total').reset_index()
# caculate unemployment rate
df_combined['Unemployment_Rate'] = df_combined['Total Unemployment'] / df_combined['Total Labor Force'] * 100

# month str to numeric
month_map_num = {'February': 2, 'August': 8}
df_combined['month_num'] = df_combined['month'].map(month_map_num)
df_combined['year_month'] = df_combined['year'].astype(str) + '-' + df_combined['month_num'].astype(str).str.zfill(2)

final_df = df_combined[['year_month', 'Unemployment_Rate']]

print(final_df)

final_df.to_csv("data_ind_youth.csv", index=False)
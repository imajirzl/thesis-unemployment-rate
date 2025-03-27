import requests
import xml.etree.ElementTree as ET
import csv

# API URL
url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_UNE_M,1.0/USA+DEU..._Z.N._T.Y_GE15..M?startPeriod=1995-01&endPeriod=2024-12"

# Send GET request
response = requests.get(url)

if response.status_code == 200 and response.text.strip():
    try:
        root = ET.fromstring(response.text)  # Parse XML response
        print("XML Data Parsed Successfully\n")

        ns = {'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}  # XML namespace

        # Open CSV file for writing
        with open("data_oecd.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Country", "Time_Period", "Unemployment_Rate"])  # Header row

            # Iterate through each country series
            for series in root.findall(".//generic:Series", namespaces=ns):
                country_code = series.find("generic:SeriesKey/generic:Value[@id='REF_AREA']", namespaces=ns).get("value")  # Get country code

                # Extract unemployment data
                for obs in series.findall("generic:Obs", namespaces=ns):
                    time_period = obs.find("generic:ObsDimension", namespaces=ns).get("value")
                    value = obs.find("generic:ObsValue", namespaces=ns).get("value")

                    # Write data to CSV
                    writer.writerow([country_code, time_period, value])

        print(f"Data successfully saved to data_oecd.csv")

    except ET.ParseError as e:
        print("XML Parse Error:", e)
else:
    print("Failed to fetch valid XML data")

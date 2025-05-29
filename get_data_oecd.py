import requests
import xml.etree.ElementTree as ET
import csv

'''
This script fetches the general unemployment data from the OECD API (USA and Germany), processes it, and saves it to a CSV file.
'''

# OECD SDMX API URL to retrieve monthly unemployment data for USA and Germany
url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_UNE_M,1.0/USA+DEU..._Z.N._T.Y_GE15..M?startPeriod=1995-01&endPeriod=2024-12"

# sending HTTP GET request to fetch the data
response = requests.get(url)

# checking if the response is successful and not emepty
if response.status_code == 200 and response.text.strip():
    try:
        # parsing the XML response content
        root = ET.fromstring(response.text)  
        print("XML Data Parsed Successfully\n")

        # defining the XML namespace used in the SDMX structure
        ns = {'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}  # XML namespace

        # opening a CSV file to write the processed data
        with open("data_oecd.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            # writing CSV header
            writer.writerow(["Country", "Time_Period", "Unemployment_Rate"])  # Header row

            # iterating through each country series
            for series in root.findall(".//generic:Series", namespaces=ns):
                # extracting the country code
                country_code = series.find("generic:SeriesKey/generic:Value[@id='REF_AREA']", namespaces=ns).get("value")  

                # extracting all unemployment data
                for obs in series.findall("generic:Obs", namespaces=ns):
                    # getting the tim e period and value
                    time_period = obs.find("generic:ObsDimension", namespaces=ns).get("value")
                    value = obs.find("generic:ObsValue", namespaces=ns).get("value")

                    # writing row to CSV
                    writer.writerow([country_code, time_period, value])

        print(f"Data successfully saved to data_oecd.csv")

    except ET.ParseError as e:
        # printing parsing error if XML is invalid
        print("XML Parse Error:", e)
else:
    # printing error if response failed or is empty
    print("Failed to fetch valid XML data")

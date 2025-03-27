import requests
import xml.etree.ElementTree as ET

# API URL (Your URL might be different)
url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_UNE_M,1.0/USA+DEU..._Z.N._T.Y_GE15..M?startPeriod=1995-01&endPeriod=2024-12"

# Send GET request
response = requests.get(url)

if response.status_code == 200 and response.text.strip():
    try:
        root = ET.fromstring(response.text)  # Parse XML response
        print("XML Data Parsed Successfully\n")

        ns = {'generic': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}  # XML namespace

        # Iterate through each series (which corresponds to a country)
        for series in root.findall(".//generic:Series", namespaces=ns):
            country_code = series.find("generic:SeriesKey/generic:Value[@id='REF_AREA']", namespaces=ns).get("value")  # Extract country code
            
            print(f"Country: {country_code}")

            # Extract unemployment data within this country's series
            for obs in series.findall("generic:Obs", namespaces=ns):
                time_period = obs.find("generic:ObsDimension", namespaces=ns).get("value")
                value = obs.find("generic:ObsValue", namespaces=ns).get("value")
                print(f"  Date: {time_period}, Unemployment Rate: {value}")

            print("\n" + "-"*50 + "\n")  # Separator for readability

    except ET.ParseError as e:
        print("XML Parse Error:", e)
else:
    print("Failed to fetch valid XML data")

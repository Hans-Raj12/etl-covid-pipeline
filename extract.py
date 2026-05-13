import requests
import json
import os

def extract_data():
    print("⏳ Extracting data from API...")

    url = "https://disease.sh/v3/covid-19/countries"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        with open("data/raw_data.json","w") as f:
            json.dump(data, f, indent=4)
        
        print(f"✅ Data extracted successfully! Total countries: {len(data)}")
        return data
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    extract_data()
    
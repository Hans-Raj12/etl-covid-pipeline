import pandas as pd 
import json

def transform_data():
    print("⏳ Transforming data...")

    with open("data/raw_data.json","r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # select only the columns we need
    df = df[[
        "country",
        "cases",
        "deaths",
        "recovered",
        "active",
        "critical",
        "tests",
        "population"
    ]]
    
    # Rename columns to be clean and professional

    df.columns = [
        "country",
        "total_cases",
        "total_deaths",
        "total_recovered",
        "active_cases",
        "critical_cases",
        "total_tests",
        "population"
    ]

    # Drop rows where country or population is missing

    df = df.dropna(subset=["country","population"])

    # Remove rows with zero population to aviod division errors

    df = df[df["population"] > 0]

    # Add calculated columns
    df["death_rate_%"] = ((df["total_deaths"] / df["total_cases"]) * 100).round(2) 
    df["recovery_rate_%"] = ((df["total_recovered"] / df['total_cases']) * 100).round(2)
    df["tests_per_million"] = ((df["total_tests"] / df["population"]) * 1_000_000).round(2)

    # Fill any remaining nulls with 0

    df = df.fillna(0)

    # save transformed data to csv
    df.to_csv("data/transformed_data.csv", index=False)

    print(f"✅ Data transformed successfully! Total rows: {len(df)}")
    print(df.head())

    return df

if __name__ == "__main__":
    transform_data()

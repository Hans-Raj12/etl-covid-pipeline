from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("🚀 Starting ETL Pipeline...")
    print("="*50)


    #step 1 - extracting data
    raw_data = extract_data()
    if raw_data is None:
        print("❌ Pipeline stopped at Extract stage.")
        return
    print("="*50)

    #step 2 - transform the extracted data
    transformed_data = transform_data()
    if transformed_data is None:
        print("❌ Pipeline stopped at Transform stage.")
        return
    print("="*50)

    #step 3 - finally load transformed data
    load_data()

    print("="*50)
    print("🎉 ETL Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
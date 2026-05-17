import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

def load_data():
    print("⏳ Loading data into prostgreSQL...")

    # Load environment variables
    load_dotenv()

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # build connection string
    if DB_PASSWORD:
        connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:
        connection_string = f"postgresql+psycopg2://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # create engine
    engine = create_engine(connection_string)

    # Load tranformed data
    df = pd.read_csv("data/transformed_data.csv")

    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS covid_data CASCADE"))
        conn.commit()

    df.to_sql(
        name="covid_data",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Data loaded successfully! {len(df)} rows inserted into 'covid_data' table.")


    # verify by querying back 
    with engine.connect() as conn:
        result = conn.execute(text("SELECT country, total_cases FROM covid_data LIMIT 5"))
        print("\n Sample data from database:")
        for row in result:
            print(row)

if __name__ == "__main__":
    load_data()
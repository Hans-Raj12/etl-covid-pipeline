#  🚀 ETL Pipeline - COVID-19 Global Data

A real-world ETL (Extract, Transform, Load) pipeline built with python, Pandas, and PostgreSQL. This project demonstrates core data engineering skills including data ingestion, transformation, and loading into a relational database.

---

## 🏗️ Project Architecture

API (disease.sh) -> Extract -> Transform -> Load -> PostgreSQL Database

---

## 🛠️ Tools & Technologies

- **Python* - Core programming language 
- **Pandas** - Data transformation and manipulation
- **SQLAlchemy** - Database connection and ORM
- **PostgreSQL** - Relational database for storing cleaned data
- **Request** - API data extraction
- **dotenv** - Secure environment variable management

---

## 📁 Project Structure

etl-covid-pipeline/
├── data/                    # Raw and transformed data (not uploaded to GitHub)
├── extract.py               # Extracts data from COVID-19 API
├── transform.py             # Cleans and transforms raw data
├── load.py                  # Loads transformed data into PostgreSQL
├── main.py                  # Runs the full ETL pipeline
├── .env                     # Database credentials (not uploaded to GitHub)
├── .gitignore               # Files excluded from GitHub
└── README.md                # Project documentation

---

## ⚙️ How to Run This Project

**1. Clone with repository**
```bash
git clone https://github.com/Hans-Raj12/etl-covid-pipeline.git
cd etl-covid-pipeline
```

**2. Install dependencies**
```bash
pip3 install pandas requests sqlalchemy psycopg2-binary python-dotenv
```

**3. Set up PostgreSQL**
```bash
psql postgres
CREATE DATABASE covid_etl;
\q
```

**4. Create your .env file**
DB_HOST=localhost
DB_PORT=5432
DB_NAME=covid_etl
DB_USER=your_username
DB_PASSWORD=

**5. Run the pipeline
```bash
python3 main.py
```

---

## 📊 What the Pipeline Does

| Stage | Description |
|---|---|
| **Extract** | Fetches live COVID-19 data for 229 countries from disease.sh API |
| **Transform** | Cleans data, selects key columns, calculates death rate, recovery rate, and tests per million |
| **Load** | Inserts cleaned data into a PostgreSQL table called `covid_data` |

---

## 📈 Key Metrics Calculated

- ** Death Rate %** - Total deaths / Total cases
- ** Recovery Rate %** - Total recovered / Total cases
- ** Tests per Million** - Total tests / population * 1,000,000

## 👨‍💻 Author

**Hans Raaj**
Transitioning from Full Stack Development (Java & Veu.js) into Data Engineering. Open to Data Engineer, ETL Developer, and Data Analyst roles.

[GitHub](https://github.com/Hans-Raj12) | [LinkedIn](https://www.linkedin.com/in/hans-raaj/)
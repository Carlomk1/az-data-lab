import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import urllib

load_dotenv()

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")

# 
params = urllib.parse.quote_plus(
    f"DRIVER=ODBC Driver 18 for SQL Server;"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=yes;")

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(connection_string)

# CSV-Datei
csv_path = "data\charging_data.csv"
df = pd.read_csv(csv_path)

# In SQL
try:
    df.to_sql("charging_stats", con=engine, if_exists="append", index=False)
    print("CSV erfolgreich geladen.")
except Exception as e:
    print("Fehler beim Upload:", e)
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

# Connection-string for SQLAlchemy + pyodbc
params = urllib.parse.quote_plus(
    f"DRIVER=ODBC Driver 18 for SQL Server;"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Load data
try:
    df = pd.read_sql("SELECT TOP 5 * FROM charging_stats;", con=engine)
    print("Daten erfolgreich geladen\n")
    print(df.head())
except Exception as e:
    print("Fehler beim Abrufen der Daten:", e)



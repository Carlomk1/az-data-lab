# az-data-lab

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="docs/logo.jpg" alt="Logo" width="300" height="150">
  </a>
</div>

## Goal & purpose
Ziel dieses Projekts ist es, eine **end-to-end Data Engineering-Umgebung auf Azure** aufzubauen – von einer relationalen SQL-Datenbank über Datenuploads bis hin zur Integration mit Databricks für spätere Analysen.  
Es wurde bewusst darauf geachtet, möglichst **kostenfrei** innerhalb eines Azure Free Trial sowie **strukturkonform (IaC-fähig)** zu arbeiten.

## Azure account
- Azure Free Trial: https://azure.microsoft.com/free/
- Account kann mit einer privaten E-Mail-Adresse erstellt werden (z. B. Gmail)
- Kreditkarte wird zur Verifizierung benötigt, es entstehen jedoch keine Kosten, solange die kostenlosen Limits nicht überschritten werden

### Overview
Grundstruktur von Azure-Diensten:
- Subscription (z. B. Free Trial)
- Resource Group (z. B. rg-dataproject1)
- Ressourcen: Azure SQL DB, Storage Account, Data Factory usw.

Dies ermöglicht eine saubere Trennung und Verwaltung der Cloud-Infrastruktur.

## SQL database creation
- Service: Azure SQL Database
- Tier: Free/Basic (vCore serverless) für Testzwecke
- WICHTIG: Bei der Authentifizierung "SQL authentication" auswählen (nicht Entra ID oder AAD)
- Benutzername/Passwort wird direkt beim Erstellen gesetzt
- Zugriff über Firewall-Regel für eigene IP und Databricks-IP gewährleisten

## Tools & Libraries

### Tools

- **ODBC Driver 18 for SQL Server**  
  Download: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

- **Python 3.11+**
- **Git** für Versionierung
- **Azure CLI** für Skripting  
  Install: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

### Python Libraries

```bash
pip install pyodbc pandas sqlalchemy python-dotenv
```

- `sqlalchemy` → für Verbindung zur DB
- `pandas` → für Datenverarbeitung
- `pyodbc` → für direkte SQL-Verbindung
- `dotenv` → für Umgebungsvariablen

---

## Setup Workflow

Ziel: End-to-End-Datenfluss in Azure mit Python aufbauen:

1. **Datenbank erstellen**
2. **Verbindung testen** (`db_connect.py`)
3. **Tabelle erstellen** (`db_create_table.py`)
4. **CSV-Daten laden** (`db_upload_data.py`)
5. **Verifizierung über Azure Portal oder Python**

### Access

- Das Skript `db_connect.py` testet die Verbindung zur SQL-Datenbank mit Umgebungsvariablen aus `.env`
- Nutzt `pyodbc` für direkten SQL-Zugriff

```python
conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)
```

### Create Table

- `db_create_table.py` enthält das `CREATE TABLE`-Statement für die Tabelle `charging_stats`
- Nutzt `pyodbc` um die Tabelle direkt in der Datenbank anzulegen

### Load Data

- `db_upload_data.py` lädt eine CSV-Datei (`charging_data.csv`) in die zuvor erstellte Tabelle
- Nutzt `pandas` + `sqlalchemy` um bulk insert durchzuführen

```python
df = pd.read_csv("charging_data.csv")
df.to_sql("charging_stats", con=engine, if_exists="append", index=False)
```

### Verify Deployment

- Im Azure Portal: öffne die SQL-Datenbank → **Query Editor (Preview)**
- Melde dich mit SQL-Login an
- Führe z. B. aus:

```sql
SELECT TOP 10 * FROM charging_stats;
```

- Alternativ: Kontrolle auch möglich via Python/Notebook (`pd.read_sql(...)`)

---

🚀


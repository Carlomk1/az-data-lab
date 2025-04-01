import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
driver = "{ODBC Driver 18 for SQL Server}"

conn = pyodbc.connect(
    f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

cursor = conn.cursor()

# schema
sql = """
CREATE TABLE charging_stats (
    year INT,
    month INT,
    chargingPower_10kW_count INT,
    chargingPower_21kW_count INT,
    chargingPower_42kW_count INT,
    chargingPower_100kW_count INT,
    chargingPower_100pluskW_count INT,
    chargingPower_AG_count INT,
    chargingPower_AG_sum INT,
    chargingPower_AI_count INT,
    chargingPower_AI_sum INT,
    chargingPower_AR_count INT,
    chargingPower_AR_sum INT,
    chargingPower_BE_count INT,
    chargingPower_BE_sum INT,
    chargingPower_BL_count INT,
    chargingPower_BL_sum INT,
    chargingPower_BS_count INT,
    chargingPower_BS_sum INT,
    chargingPower_CH_count INT,
    chargingPower_CH_sum INT,
    chargingPower_FR_count INT,
    chargingPower_FR_sum INT,
    chargingPower_GE_count INT,
    chargingPower_GE_sum INT,
    chargingPower_GL_count INT,
    chargingPower_GL_sum INT,
    chargingPower_GR_count INT,
    chargingPower_GR_sum INT,
    chargingPower_JU_count INT,
    chargingPower_JU_sum INT,
    chargingPower_LU_count INT,
    chargingPower_LU_sum INT,
    chargingPower_NE_count INT,
    chargingPower_NE_sum INT,
    chargingPower_NW_count INT,
    chargingPower_NW_sum INT,
    chargingPower_OW_count INT,
    chargingPower_OW_sum INT,
    chargingPower_SG_count INT,
    chargingPower_SG_sum INT,
    chargingPower_SH_count INT,
    chargingPower_SH_sum INT,
    chargingPower_SO_count INT,
    chargingPower_SO_sum INT,
    chargingPower_SZ_count INT,
    chargingPower_SZ_sum INT,
    chargingPower_TG_count INT,
    chargingPower_TG_sum INT,
    chargingPower_TI_count INT,
    chargingPower_TI_sum INT,
    chargingPower_UR_count INT,
    chargingPower_UR_sum INT,
    chargingPower_VD_count INT,
    chargingPower_VD_sum INT,
    chargingPower_VS_count INT,
    chargingPower_VS_sum INT,
    chargingPower_ZG_count INT,
    chargingPower_ZG_sum INT,
    chargingPower_ZH_count INT,
    chargingPower_ZH_sum INT,
    locations_AG_count INT,
    locations_AI_count INT,
    locations_AR_count INT,
    locations_BE_count INT,
    locations_BL_count INT,
    locations_BS_count INT,
    locations_CH_count INT,
    locations_FR_count INT,
    locations_GE_count INT,
    locations_GL_count INT,
    locations_GR_count INT,
    locations_JU_count INT,
    locations_LU_count INT,
    locations_NE_count INT,
    locations_NW_count INT,
    locations_OW_count INT,
    locations_SG_count INT,
    locations_SH_count INT,
    locations_SO_count INT,
    locations_SZ_count INT,
    locations_TG_count INT,
    locations_TI_count INT,
    locations_UR_count INT,
    locations_VD_count INT,
    locations_VS_count INT,
    locations_ZG_count INT,
    locations_ZH_count INT,
    plugs_AVCONConnector_count INT,
    plugs_CCSCombo1PlugCableAttached_count INT,
    plugs_CCSCombo2PlugCableAttached_count INT,
    plugs_CH_count INT,
    plugs_CHAdeMO_count INT,
    plugs_IEC60309SinglePhase_count INT,
    plugs_IEC60309ThreePhase_count INT,
    plugs_LargePaddleInductive_count INT,
    plugs_NEMA520_count INT,
    plugs_SmallPaddleInductive_count INT,
    plugs_TeslaConnector_count INT,
    plugs_Type1ConnectorCableAttached_count INT,
    plugs_Type2ConnectorCableAttached_count INT,
    plugs_Type2Outlet_count INT,
    plugs_Type3Outlet_count INT,
    plugs_TypeEFrenchStandard_count INT,
    plugs_TypeFSchuko_count INT,
    plugs_TypeGBritishStandard_count INT,
    plugs_TypeJSwissStandard_count INT,
    plugs_Unspecified_count INT,
    stations_AG_count INT,
    stations_AI_count INT,
    stations_AR_count INT,
    stations_BE_count INT,
    stations_BL_count INT,
    stations_BS_count INT,
    stations_CH_count INT,
    stations_FR_count INT,
    stations_GE_count INT,
    stations_GL_count INT,
    stations_GR_count INT,
    stations_JU_count INT,
    stations_LU_count INT,
    stations_NE_count INT,
    stations_NW_count INT,
    stations_OW_count INT,
    stations_SG_count INT,
    stations_SH_count INT,
    stations_SO_count INT,
    stations_SZ_count INT,
    stations_TG_count INT,
    stations_TI_count INT,
    stations_UR_count INT,
    stations_VD_count INT,
    stations_VS_count INT,
    stations_ZG_count INT,
    stations_ZH_count INT
);
"""

try:
    cursor.execute(sql)
    conn.commit()
    print("✅ Tabelle 'charging_stats' erfolgreich erstellt.")
except Exception as e:
    print("❌ Fehler beim Erstellen der Tabelle:", e)
finally:
    cursor.close()
    conn.close()
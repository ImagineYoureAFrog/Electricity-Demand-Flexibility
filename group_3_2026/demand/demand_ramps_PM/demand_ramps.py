import pandas as pd

france = pd.read_csv(
    "group_3_2026/data/raw/France_demand_year_2024.csv",
    sep="\t",
    encoding="latin1"
)

spain_1 = pd.read_csv(
    "group_3_2026/data/raw/Spain-2024-05-10-Seguimiento de la demanda de energía eléctrica (MW).csv",
    skiprows=2,
    encoding="latin1",
    header=None,
    usecols=[0, 1]
)

spain_2 = pd.read_csv(
    "group_3_2026/data/raw/Spain-2024-05-11-Seguimiento de la demanda de energía eléctrica (MW).csv",
    skiprows=2,
    encoding="latin1",
    header=None,
    usecols=[0, 1]
)

spain_3 = pd.read_csv(
    "group_3_2026/data/raw/Spain-2024-05-12-Seguimiento de la demanda de energía eléctrica (MW).csv",
    skiprows=2,
    encoding="latin1",
    header=None,
    usecols=[0, 1]
)

spain_4 = pd.read_csv(
    "group_3_2026/data/raw/Spain-2024-05-13-Seguimiento de la demanda de energía eléctrica (MW).csv",
    skiprows=2,
    encoding="latin1",
    header=None,
    usecols=[0, 1]
)
spain = pd.concat([spain_1, spain_2, spain_3, spain_4])

france_clean = france[["Date", "Heures", "Consommation"]].copy()
france_clean["datetime"] = pd.to_datetime(
    france_clean["Date"].astype(str) + " " + france_clean["Heures"].astype(str),
    errors="coerce"
)
france_clean["demand"] = pd.to_numeric(france_clean["Consommation"], errors="coerce")
france_clean["country"] = "France"
france_clean = france_clean[["country", "datetime", "demand"]]

spain_clean = spain.copy()
spain_clean.columns = ["datetime", "demand"]
spain_clean["datetime"] = pd.to_datetime(spain_clean["datetime"], errors="coerce")
spain_clean["demand"] = pd.to_numeric(spain_clean["demand"], errors="coerce")
spain_clean["country"] = "Spain"
spain_clean = spain_clean[["country", "datetime", "demand"]]
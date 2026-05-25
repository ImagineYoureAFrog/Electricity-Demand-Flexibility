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

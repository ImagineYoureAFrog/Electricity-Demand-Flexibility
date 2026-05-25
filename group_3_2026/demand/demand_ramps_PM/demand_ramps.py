import os
import pandas as pd

# loading the cleaned data for France, Germany, and Spain
df_fr = pd.read_csv("data\\processed\\france_cleaned.csv")
df_de = pd.read_csv("data\\processed\\germany_cleaned.csv")
df_es = pd.read_csv("data\\processed\\spain_cleaned.csv")
# Ensure data is sorted by time
df_fr = df_fr.sort_values(by='timestamp').reset_index(drop=True)
df_de = df_de.sort_values(by='timestamp').reset_index(drop=True)
df_es = df_es.sort_values(by='timestamp').reset_index(drop=True)
# Calculate the hourly ramp
df_fr['rampa'] = df_fr['demand'].diff()
df_de['rampa'] = df_de['demand'].diff()
df_es['rampa'] = df_es['demand'].diff()

print("¡Rampas calculadas con éxito!")



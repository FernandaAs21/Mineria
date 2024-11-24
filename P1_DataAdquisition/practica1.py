import pandas as pd
from tabulate import tabulate

# Leer el archivo CSV correctamente
df = pd.read_csv('charts.csv')

print(tabulate(df, headers='keys', tablefmt='pretty'))
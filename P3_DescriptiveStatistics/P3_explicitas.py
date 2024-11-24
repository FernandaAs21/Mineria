import pandas as pd
import os

# Leer el archivo de países (diccionario de códigos de país)
country_df = pd.read_csv('countries.csv')

# Crear un diccionario para convertir los códigos de país a nombres completos
country_dict = dict(zip(country_df['code'], country_df['country']))

# Cargar los datos del archivo CSV
df = pd.read_csv('charts_df.csv')

# Crear carpeta para guardar los csv's
output_folder = 'P3_CSVs'
# si no existe
os.makedirs(output_folder, exist_ok=True)

# Filtrar las canciones explícitas
explicit_df = df[df['explicit'] == True]

# Contar cuántas canciones explícitas hay por país
explicit_country_count = explicit_df['country'].value_counts()

# Convertir la serie resultante a un DataFrame
explicit_country_df = explicit_country_count.reset_index()
explicit_country_df.columns = ['country_code', 'explicit_count']

# Mapear los códigos de país a los nombres completos usando el diccionario
explicit_country_df['country'] = explicit_country_df['country_code'].map(country_dict)

# Guardar los resultados en un CSV
explicit_country_df.to_csv(os.path.join(output_folder, 'paises_explicitas.csv'), index=False)


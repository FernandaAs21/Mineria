import pandas as pd
import os

# Cargar los datos del archivo CSV
df = pd.read_csv('charts_df.csv')

# Crear carpeta para guardar los csv's
output_folder = 'P3_CSVs'
# si no existe
os.makedirs(output_folder, exist_ok=True)

# Limpiar los nombres de los países
df['country'] = df['country'].str.strip()

# Leer el archivo de países (diccionario de códigos de país)
country_df = pd.read_csv('countries.csv')

# Crear un diccionario para convertir los códigos de país a nombres completos
country_dict = dict(zip(country_df['code'], country_df['country']))

# Mapear los códigos de país a los nombres completos usando el diccionario
df['country'] = df['country'].map(country_dict)

# Contar los géneros musicales diferentes por país
genres_by_country = df.groupby('country')['artist_genres'].nunique().reset_index()

# Renombrar las columnas para mayor claridad
genres_by_country.columns = ['Country', 'Unique Genres']

# Guardar los resultados en un archivo CSV
genres_by_country.to_csv(os.path.join(output_folder, 'generos_paises.csv'), index=False)


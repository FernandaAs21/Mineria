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

# Calcular el promedio de duración de las canciones por país en segundos y luego convertir a minutos
average_duration_per_country = df.groupby('country')['duration'].mean().reset_index()

# Convertir la duración de segundos a minutos
average_duration_per_country['Average Duration (minutes)'] = (average_duration_per_country['duration'] / 60).round(2)
                                                              

# Eliminar la columna original de duración en segundos (opcional)
average_duration_per_country = average_duration_per_country.drop(columns=['duration'])

# Seleccionar los 10 países con la mayor duración promedio
average_duration_per_country = average_duration_per_country.nlargest(10, 'Average Duration (minutes)')

# Guardar los resultados en un archivo CSV
average_duration_per_country.to_csv(os.path.join(output_folder, 'duracionPromedio.csv'), index=False)

print(average_duration_per_country.head())
print(average_duration_per_country.info())
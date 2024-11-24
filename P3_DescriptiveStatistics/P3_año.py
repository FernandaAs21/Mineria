import pandas as pd
import os

# Cargar los datos del archivo CSV
df = pd.read_csv('charts_df.csv')

# Crear carpeta para guardar los csv's
output_folder = 'P3_CSVs'
# si no existe
os.makedirs(output_folder, exist_ok=True)

# Filtrar los registros solo del país 'us' (Estados Unidos)
df_us = df[df['country'] == 'us'].copy()

# Convertir la columna 'date' a formato datetime, manejando múltiples formatos y errores
df_us['date'] = pd.to_datetime(df_us['date'], format='mixed', errors='coerce')

# Eliminar filas con fechas inválidas que no pudieron ser convertidas
df_us = df_us.dropna(subset=['date'])

# Crear una nueva columna 'year' con el año extraído de la fecha
df_us['year'] = df_us['date'].dt.year

# Obtener la canción con la mejor posición por año (menor número en 'position')
most_popular_per_year_us = df_us.loc[df_us.groupby('year')['position'].idxmin()]

most_popular_per_year_us = most_popular_per_year_us[['year', 'name', 'streams']]

# Guardar el resultado en un nuevo archivo CSV
most_popular_per_year_us.to_csv(os.path.join(output_folder, 'canciones_mas_populares_us_por_año.csv'), index=False)
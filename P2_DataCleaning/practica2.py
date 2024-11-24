import pandas as pd

# Cargar el CSV
df = pd.read_csv('charts.csv')

# Seleccionar 5500 filas aleatorias
df = df.sample(n=5500, random_state=42)

# Reduccion de columnas
df = df.drop(['track_id'], axis=1)

# Eliminar filas si existen valores nulos en alguna columna
df = df.dropna()

# Eliminar filas que contengan una celda con el valor: []
df = df[~df.apply(lambda row: row.astype(str).str.contains(r'\[\]').any(), axis=1)]

# Eliminar corchetes y comillas de la columna 'artists'
df['artists'] = df['artists'].str.replace(r"[\[\]']", "", regex=True)
df['artist_genres'] = df['artist_genres'].str.replace(r"[\[\]']", "", regex=True)

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df.to_csv('charts_df.csv', index=False)

df.info()
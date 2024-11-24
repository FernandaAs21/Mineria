import pandas as pd
from scipy.stats import kruskal

# Cargar el archivo con el diccionario de países
countries_dict = pd.read_csv('countries.csv')

# Cargar el archivo principal
df = pd.read_csv('charts_df.csv')

# Realizar el merge para obtener el nombre completo de los países
df = df.merge(countries_dict, left_on='country', right_on='code', how='left')

# Verifica si existe una nueva columna con el nombre de los países
if 'country_y' in df.columns:
    df['country'] = df['country_y']
elif 'country' in df.columns:
    pass  # ya está bien
else:
    raise KeyError("No se encontró una columna de países después del merge.")

# Agrupar por el nombre del país y aplicar la prueba de Kruskal-Wallis en 'streams'
groups = [group['streams'].dropna() for name, group in df.groupby('country')]

# Realizar la prueba de Kruskal-Wallis
stat, p_value = kruskal(*groups)

# Mostrar resultados
print(f'Estadístico H: {stat}')
print(f'P-valor: {p_value}')

# Interpretación básica del p-valor
if p_value < 0.05:
    print("Hay una diferencia significativa entre los países.")
else:
    print("No hay evidencia suficiente de una diferencia significativa entre los países.")


# Separar las canciones en explícitas y no explícitas
explicit_streams = df[df['explicit'] == True]['streams'].dropna()
non_explicit_streams = df[df['explicit'] == False]['streams'].dropna()

# Realizar la prueba de Kruskal-Wallis
stat, p_value = kruskal(explicit_streams, non_explicit_streams)

# Mostrar resultados
print(f'Estadístico H: {stat}')
print(f'P-valor: {p_value}')

# Interpretación básica del p-valor
if p_value < 0.05:
    print("Hay una diferencia significativa en los streams entre canciones explícitas y no explícitas.")
else:
    print("No hay evidencia suficiente de una diferencia significativa en los streams entre canciones explícitas y no explícitas.")


# Agrupar por el género del artista y obtener la duración de las canciones
groups = [group['duration'].dropna() for name, group in df.groupby('artist_genres')]

# Realizar la prueba de Kruskal-Wallis
stat, p_value = kruskal(*groups)

# Mostrar resultados
print(f'Estadístico H: {stat}')
print(f'P-valor: {p_value}')

# Interpretación básica del p-valor
if p_value < 0.05:
    print("Hay una diferencia significativa en la duración de las canciones entre los géneros de artistas.")
else:
    print("No hay evidencia suficiente de una diferencia significativa en la duración de las canciones entre los géneros de artistas.")

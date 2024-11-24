import pandas as pd
import os

# Diccionario para mapear los códigos de país a nombres completos
country_names = {
    "hn": "Honduras",
    "ua": "Ukraine",
    "lv": "Latvia",
    "ar": "Argentina",
    "fr": "France",
    "mx": "Mexico",
    "us": "United States",
    "es": "Spain",
    "br": "Brazil",
    "ca": "Canada",
    "de": "Germany",
    "it": "Italy",
    "jp": "Japan",
    "ru": "Russia",
    "au": "Australia",
    "in": "India",
    "cn": "China",
    "uk": "United Kingdom",
    "nl": "Netherlands",
    "se": "Sweden",
    "no": "Norway",
    "dk": "Denmark",
    "fi": "Finland",
    "be": "Belgium",
    "pt": "Portugal",
    "pl": "Poland",
    "gr": "Greece",
    "cz": "Czech Republic",
    "ch": "Switzerland",
    "at": "Austria",
    "ie": "Ireland",
    "sg": "Singapore",
    "nz": "New Zealand",
    "za": "South Africa",
    "kr": "South Korea",
    "id": "Indonesia",
    "ph": "Philippines",
    "th": "Thailand",
    "my": "Malaysia",
    "vn": "Vietnam",
    "il": "Israel",
    "tr": "Turkey",
    "cl": "Chile",
    "co": "Colombia",
    "pe": "Peru",
    "ve": "Venezuela",
    "uy": "Uruguay",
    "ec": "Ecuador",
    "cr": "Costa Rica",
    "pa": "Panama",
    "gt": "Guatemala",
    "do": "Dominican Republic",
    "pr": "Puerto Rico"
 }


# Cargar los datos del archivo CSV
df = pd.read_csv('charts_df.csv')

# Crear carpeta para guardar los csv's
output_folder = 'P3_CSVs'
# si no existe
os.makedirs(output_folder, exist_ok=True)

# Eliminar filas donde el país sea 'global'
df = df[df['country'] != 'global']

# Convertir la columna 'date' a formato datetime
df['date'] = pd.to_datetime(df['date'], format='mixed', errors='coerce')

# Eliminar filas con fechas inválidas
df = df.dropna(subset=['date'])

# Crear una nueva columna 'year' con el año extraído de la fecha
df['year'] = df['date'].dt.year

# Reemplazar los códigos de país por nombres completos
df['country'] = df['country'].map(country_names)

# Agrupar por año y país, sumando los streams
streams_by_country_year = df.groupby(['year', 'country'])['streams'].sum().reset_index()

# Obtener el país con más reproducciones por año
top_country_per_year = streams_by_country_year.loc[streams_by_country_year.groupby('year')['streams'].idxmax()]

# Guardar el resultado en un nuevo archivo CSV
top_country_per_year.to_csv(os.path.join(output_folder, 'paises_con_mas_reproducciones_por_año.csv'), index=False)

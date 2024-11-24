import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Se define la carpeta donde estan los archivos CSV
folder = 'P3_CSVs/'

csv_files = {
    "Canciones_mas_populares_us_por_año": 'canciones_mas_populares_us_por_año.csv',
    "duracionPromedio": 'duracionPromedio.csv',
    "generos_paises": 'generos_paises.csv',
    "paises_explicitas": 'paises_explicitas.csv',
    "paises_con_mas_reproducciones_por_año": 'paises_con_mas_reproducciones_por_año.csv'
}
# Cargar los archivos CSV en df
dataframes = {key: pd.read_csv(os.path.join(folder, file)) for key, file in csv_files.items()}

# Crear carpeta para guardar las imagenes
output_folder = 'P3_PNGs'
# si no existe
os.makedirs(output_folder, exist_ok=True)

# Crear una gráfica de barras mostrando las canciones con más streams cada año
#plt.figure(figsize=(10, 6))
#sns.barplot(data=df, x='year', y='streams', hue='name', dodge=False)

# Agregar título y etiquetas
#plt.title('Streams por Canción en Cada Año (US)', fontsize=14)
#plt.xlabel('Año', fontsize=12)
#plt.ylabel('Streams', fontsize=12)

# Mejorar la visualización de la gráfica
#plt.xticks(rotation=45)
#plt.tight_layout()

# Guardar la gráfica como imagen
#plt.savefig('streams_por_cancion.png', dpi=300)

# Función para generar gráficos
def generate_visualizations():
    # Crear gráficos con cada archivo
    for title, df in dataframes.items():
        plt.figure(figsize=(8, 5))
        
        # Diferentes tipos de gráficos según el tipo de datos
        if "Canciones_mas_populares_us_por_año" in title:
            # Histograma
            sns.histplot(df["streams"], kde=True, color='blue')
            plt.title("Histograma: Canciones_mas_populares_us_por_año")
        
        elif "duracionpromedio" in title:
            # grafico de barras
            top_countries = df.groupby("country")["Average Duration (minutes)"].mean().nlargest(10).index
            df_top = df[df["country"].isin(top_countries)]

            plt.figure(figsize=(12, 6))
            sns.boxplot(data=df_top, x="country", y="Average Duration (minutes)", palette="Set3")
            plt.title("Distribución de Duración Promedio por País (Top 10)")
            plt.xlabel("País")
            plt.ylabel("Duración Promedio (minutos)")
            plt.xticks(rotation=90)
            plt.show()
        
        elif "paises_explicitas" in title:
            # Diagrama de dispersión
            sns.scatterplot(data=df, x="country", y="explicit_count", color='green')
            plt.xlabel("paises")
            plt.ylabel("Canciones Explicitas")
        
        elif "generos_paises" in title:
            # Grafico de barras horizontal
            df_sorted = df.sort_values(by="Unique Genres", ascending=True)
            plt.figure(figsize=(12, 16))
            plt.barh(df_sorted["Country"], df_sorted["Unique Genres"], color="skyblue", edgecolor="black")
            plt.title("Número de Géneros Únicos por País", fontsize=16)
            plt.xlabel("Número de Géneros Únicos", fontsize=12)
            plt.ylabel("País", fontsize=12)
            for index, value in enumerate(df_sorted["Unique Genres"]):
                plt.text(value + 1, index, str(value), va="center", fontsize=10)
        
        elif "paises_con_mas_reproducciones_por_año" in title:
            # Gráfico de líneas
            sns.lineplot(data=df, x="year", y="streams", marker="o", color='red')
            plt.title("reproducciones por año")
            plt.xlabel("Año")
            plt.ylabel("streams")
        
        # Guardar cada gráfico como archivo en la carpeta de gráficos
        plt.tight_layout()
        output_path = os.path.join(output_folder, f"{title.replace(' ', '_').lower()}_grafico.png")
        plt.savefig(output_path)
        plt.close()
        print(f"Gráfico guardado: {output_path}")

# Generar visualizaciones
generate_visualizations()





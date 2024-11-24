import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Cargar el archivo CSV con los datos de las canciones
df = pd.read_csv('charts_df.csv')

# Suponiendo que la columna de texto es 'name' (o el nombre que contenga texto relevante)
# Unimos todos los nombres de las canciones en una sola cadena
text = ' '.join(df['name'].dropna())  # Usamos dropna() para eliminar valores nulos

# Crear la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # No mostrar los ejes
plt.title('Nube de Palabras de los Nombres de Canciones', fontsize=16)
plt.show()

# Guardar la imagen si es necesario
wordcloud.to_file('nube_de_palabras_canciones.png')
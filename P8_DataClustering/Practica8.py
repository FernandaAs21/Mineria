import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Cargamos el CSV
df = pd.read_csv('charts_df.csv')

# Preprocesamiento
df['explicit_num'] = df['explicit'].apply(lambda x: 1 if x == 'True' else 0)  # Convertimos 'explicit' a 1 y 0
df['streams_log'] = np.log1p(df['streams'])  # Aplicamos logaritmo a 'streams'

# Seleccionamos las características para el modelo
X = df[['streams_log', 'duration']]  # Usamos 'streams' y 'duration' como características

# Escalamos las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Creamos y entrenamos el modelo KMeans
kmeans = KMeans(n_clusters=3, random_state=42)  # Se elige 3 clusters (puedes ajustarlo según el problema)
kmeans.fit(X_scaled)

# Añadimos las etiquetas de los clusters al DataFrame
df['cluster'] = kmeans.labels_

# Evaluamos el modelo visualmente con un gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['cluster'], cmap='viridis', s=30)
plt.title('Clustering de los Datos de Entrenamiento (Streams vs Duration)', fontsize=16)
plt.xlabel('Streams Escalados')
plt.ylabel('Duración Escalada')
plt.colorbar(label='Número del Cluster')

# Guardamos la imagen
plt.savefig('clustering_plot.png')

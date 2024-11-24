import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Cargamos el CSV
df = pd.read_csv('charts_df.csv')

# Preprocesamiento
df['explicit_num'] = df['explicit'].apply(lambda x: 1 if x == 'True' else 0)  # Convertimos 'explicit' a 1 y 0
df['streams_log'] = np.log1p(df['streams'])  # Aplicamos logaritmo a 'streams'

# Seleccionamos las características para el modelo
X = df[['streams_log', 'duration']]  # Usamos 'streams' y 'duration' como características
y = df['explicit_num']  # Etiquetas: si es explícito o no

# Dividimos los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalamos las características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Creamos y entrenamos el modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

# Hacemos predicciones
y_pred = knn.predict(X_test_scaled)

# Evaluamos el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Graficamos el scatter para observar la relación entre las dos características
plt.figure(figsize=(10, 6))
plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=y_train, cmap='viridis', s=30)
plt.title('Scatter Plot de los Datos de Entrenamiento (Streams vs Duration)', fontsize=16)
plt.xlabel('Streams Escalados')
plt.ylabel('Duración Escalada')
plt.colorbar(label='Valor Original de la Clase')

# Guardamos la imagen
plt.savefig('scatter_plot_entrenamiento.png', dpi=300)  # Guarda la imagen en formato PNG con calidad 300 dpi

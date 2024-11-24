import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# Leer el archivo CSV correctamente
df = pd.read_csv('charts.csv')

# Convertir la columna 'date' al formato de fecha
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Asegurarnos de que no haya valores nulos en las fechas
df = df.dropna(subset=['date'])

# Agrupar los datos por mes y calcular el total de streams
df['year_month'] = df['date'].dt.to_period('M')
monthly_streams = df.groupby('year_month')['streams'].sum().reset_index()
monthly_streams['year_month'] = monthly_streams['year_month'].astype(str)

# Convertir fechas a números para la regresión lineal (e.g., número de meses desde el inicio)
monthly_streams['time_index'] = np.arange(len(monthly_streams))

# Dividir los datos en conjunto de entrenamiento y prueba
X = monthly_streams[['time_index']]
y = monthly_streams['streams']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)

# Visualizar los datos reales y las predicciones
plt.figure(figsize=(12, 6))
plt.plot(monthly_streams['time_index'], monthly_streams['streams'], label='Datos reales', marker='o')
plt.plot(X_test['time_index'], y_pred, label='Predicciones', linestyle='--', color='red')
plt.title('Predicción de Streams Mensuales')
plt.xlabel('Índice de Tiempo (Meses desde inicio)')
plt.ylabel('Streams')
plt.legend()
plt.show()
plt.savefig('Predicción de Streams Mensuales.png', dpi=300, bbox_inches='tight')
mse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Cargar el archivo principal
df = pd.read_csv('charts_df.csv')

# Eliminar filas con valores nulos en las columnas necesarias
df = df[['streams', 'duration']].dropna()

# Definir variable dependiente (Y) e independiente (X)
X = df[['duration']]  # Duración de la canción
y = df['streams']  # Streams (reproducciones)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo lineal
model = LinearRegression()

# Ajustar el modelo a los datos de entrenamiento
model.fit(X_train, y_train)

# Predecir los valores de y para el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el R² score
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')

# Guardar gráficos

# Gráfico de dispersión con la línea de regresión ajustada
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Línea de regresión')
plt.title('Regresión Lineal: Streams vs Duration')
plt.xlabel('Duration (segundos)')
plt.ylabel('Streams (reproducciones)')
plt.legend()
plt.savefig('regresion_lineal_streams_vs_duration.png')
plt.close()




# Eliminar filas con valores nulos
df = df[['streams', 'date']].dropna()

# Extraer el año de la columna de fechas
df['year'] = pd.to_datetime(df['date']).dt.year

# Definir variables
X = df[['year']]  # Año
y = df['streams']  # Streams

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# R²
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')

# Guardar gráfico
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Línea de regresión')
plt.title('Regresión Lineal: Streams vs Year')
plt.xlabel('Year')
plt.ylabel('Streams')
plt.legend()
plt.savefig('regresion_lineal_streams_vs_year.png')
plt.close()

# Eliminar filas con valores nulos
df = df[['streams', 'position']].dropna()

# Definir variables
X = df[['position']]  # Posición
y = df['streams']  # Streams

# Dividir los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# R²
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')

# Guardar gráfico
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Línea de regresión')
plt.title('Regresión Lineal: Streams vs Position')
plt.xlabel('Position')
plt.ylabel('Streams')
plt.legend()
plt.savefig('regresion_lineal_streams_vs_position.png')
plt.close()

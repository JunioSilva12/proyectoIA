# Importar las bibliotecas necesarias
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Crear un DataFrame con datos ficticios (puedes reemplazarlos con tus propios datos)
data = {
    'Calificacion1': [80, 85, 75, 90, 95],
    'Calificacion2': [70, 75, 65, 80, 85],
    'PromedioAnterior': [82, 86, 77, 88, 92],
    'Rendimiento': [85, 88, 78, 91, 94]  # Rendimiento académico esperado
}

df = pd.DataFrame(data)

# Separar las características (X) y la variable objetivo (y)
X = df.drop('Rendimiento', axis=1)
y = df['Rendimiento']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo de regresión lineal
#model = LinearRegression()
model = svm.SVR(kernel='linear', C=1.0)
model.fit(X_train, y_train)


# Realizar predicciones en el conjunto de prueba
predictions = model.predict(X_test)
#print(predictions)
# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, predictions)
print(f'Error cuadrático medio: {mse}')

# Guardar el modelo entrenado para su uso futuro
joblib.dump(model, 'modelo_rendimiento_academico.pkl')

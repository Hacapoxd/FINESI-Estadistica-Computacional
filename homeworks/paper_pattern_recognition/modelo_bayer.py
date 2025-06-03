import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

# Leer archivo CSV
df = pd.read_csv("denunciados.csv", delimiter=';')

# Seleccionar columnas relevantes y limpiar
cols = ['dpto_pjfs', 'prov_pjfs', 'dist_pjfs', 'especialidad', 'tipo_caso', 'subgenerico']
df_model = df[cols].dropna()

# Codificar categorías
label_encoders = {}
for col in df_model.columns:
    le = LabelEncoder()
    df_model[col] = le.fit_transform(df_model[col])
    label_encoders[col] = le

# Variables predictoras y objetivo
X = df_model.drop("subgenerico", axis=1)
y = df_model["subgenerico"]

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar modelo Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)



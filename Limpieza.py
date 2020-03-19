import pandas as pd
import numpy as np

dataset = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv")

headers = ["Factor de Riesgo", "Devaluacion por año", "Marca", "Combustible", "Turbo-Estandar", "Numero de Puertas",
           "Carroceria",
           "Traccion de la Rueda", "Ubicacion del motor ", "Distancia entre ejes", "Longitud", "Ancho", "Altura",
           "Peso del Vehiculo", "Tipo de Motor",
           "Numero de Cilindros", "Tamaño del Motor", "Sistema de Combustible", "Diametro del cilindro",
           "Radio del Cilindro", "Relacion de Compresion", "Caballos de Fuerza",
           "Revoluciones por minuto", "Millas en Ciudad", "Millas en carretera", "Precio"]

df = pd.read_csv(dataset, names=headers)

df.replace("?", np.nan, inplace=True)  # cambio los ? por NAN

missing_data = df.isnull()  # Verificar valores nulos

for column in missing_data.columns.values.tolist():  # TRUE = Valores nulos
    print(column)
    print(missing_data[column].value_counts())
    print("")

avg_norm_loss = df["Devaluacion por año"].astype("float").mean(axis=0)  # Promedio de la columna
print("Promedio :Devaluacion por año", avg_norm_loss)
df["Devaluacion por año"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore = df['Diametro del cilindro'].astype('float').mean(axis=0)
print("Promedio:Diametro del cilindro", avg_bore)
df["Diametro del cilindro"].replace(np.nan, avg_bore, inplace=True)

avg_stroke = df["Radio del Cilindro"].astype("float").mean(axis=0)
print("Promedio:Radio del Cilindro", avg_stroke)
df["Radio del Cilindro"].replace(np.nan, avg_stroke, inplace=True)

avg_horsepower = df['Caballos de Fuerza'].astype('float').mean(axis=0)
print("Promedio: Caballos de Fuerza", avg_horsepower)
df['Caballos de Fuerza'].replace(np.nan, avg_horsepower, inplace=True)

avg_peakrpm = df['Revoluciones por minuto'].astype('float').mean(axis=0)
print("Promedio: Revoluciones por Minuto", avg_peakrpm)
df['Revoluciones por minuto'].replace(np.nan, avg_peakrpm, inplace=True)

df['Numero de Puertas'].value_counts()

df["Numero de Puertas"].replace(np.nan, "four", inplace=True)

# El precio no lo puedo promediar por ser la variable objetivo, toca eliminar

df.dropna(subset=["Precio"], axis=0, inplace=True)

df.reset_index(drop=True, inplace=True)

df[["Diametro del cilindro", "Radio del Cilindro"]] = df[["Diametro del cilindro", "Radio del Cilindro"]].astype(
    "float")
df[["Devaluacion por año"]] = df[["Devaluacion por año"]].astype("int")
df[["Precio"]] = df[["Precio"]].astype("float")
df[["Revoluciones por minuto"]] = df[["Revoluciones por minuto"]].astype("float")

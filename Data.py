import pandas as pd

dataset = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv'

headers = ["Factor de Riesgo", "Devaluacion por año", "Marca", "Combustible", "Turbo-Estandar", "Numero de Puertas",
           "Carroceria",
           "Traccion de la Rueda", "Ubicacion del motor ", "Distancia entre ejes", "Longitud", "Ancho", "Altura",
           "Peso del Vehiculo", "Tipo de Motor",
           "Numero de Cilindros", "Tamaño del Motor", "Sistema de Combustible", "Diametro del cilindro",
           "Radio del Cilindro", "Relacion de Compresion", "Caballos de Fuerza",
           "Revoluciones por minuto", "Millas en Ciudad", "Millas en carretera", "Precio"]

df = pd.read_csv(dataset, names=headers)
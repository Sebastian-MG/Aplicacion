import pandas as pd
import numpy as np
from Data import df

class Limpieza:
    def __init__(self):
        self.df = df

    def datos_perdidos(self):
        missing_data = df.isnull()
        for column in missing_data.columns.values.tolist():  # TRUE = Valores nulos
            print(column)
            print(missing_data[column].value_counts())
            print("")
        df.replace("?", np.nan, inplace=True)
        return missing_data

    def eliminar_filas(self):
        df.dropna(subset=["Precio"], axis=0, inplace=True)
        df.reset_index(drop=True, inplace=True)

    def llenar_promedio(self):

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



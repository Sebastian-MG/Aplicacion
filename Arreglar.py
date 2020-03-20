from calendar import different_locale

import pandas as pd
import numpy as np
import math
import csv
import os


class arre():
    def __init__(self, df):
        self.vector = []

    def reparaCSV(self):
        with  open('pruebaas.csv', newline='') as File:
            reader = csv.reader(File)
            i=0
            f=''
            for row in reader:

                if i > 1:
                    f = str(row).replace("[\"", '').replace('n', '').replace('\'', '').replace('b', '').replace('\\', '').replace('r', '').replace(' ', '').replace("0\n" + str(i) , ' ').replace("\"]", '')
                    f=f.replace("[", '').replace("]", '')
                    vec=self.separar(f)
                    self.generarpd(vec)

                else:
                    nombres  = str(row).replace("[\"", '').replace('n', '').replace('\'', '').replace('b', '').replace('\\', '').replace('r', '').replace(' ', '').replace("0\n" + str(i) , ' ').replace("\"]", '')
                    nombres=nombres.replace("[", '').replace("]", '')
                    nomb = self.separar(nombres)
                i=i+1
        return pd.DataFrame(self.vector,columns=nomb).astype('float')

    def separar(self,vec):
        return vec.split(',')

    def generarpd(self,dt):
        self.vector.append(dt)

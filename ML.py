import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report

class Metodo():
    def __init__(self):
        self.estado = 'Procesando los datos'

    def KNN():

        return KNeighborsClassifier()

    def svc():

        return SVC(C=100)

    def LG():

        return LogisticRegression()

    def ann():

        return MLPClassifier()


class Proceso(Metodo):
    def __init__(self, df, semi, sco, testeo, metodo,pre):
        self.seedc = semi
        self.scorec = sco
        self.validation_size = testeo
        self.x = df.iloc[:, :len(df.T) - 1]
        self.y = df.iloc[:, len(df.T) - 1: len(df.T)]
        self.proceso = metodo
        self.prediccion=pre



    def it(self, seed=0, score=0):
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=self.validation_size,
                                                            random_state=seed)

        self.proceso.fit(x_train, y_train)
        if score <= self.scorec and seed <= self.seedc:
            return self.it(seed=seed + 1,score = self.proceso.score(x_test, y_test))
        else:
            return confusion_matrix(y_test, self.proceso.predict(x_test)), precision_score(y_test,
                                                                                           self.proceso.predict(x_test),
                                                                                           average=None), recall_score(
                y_test, self.proceso.predict(x_test), average=None), f1_score(y_test, self.proceso.predict(x_test),
                                                                              average=None), accuracy_score(y_test,
                                                                                                            self.proceso.predict(
                                                                                                                x_test)), score, self.proceso.predict(self.prediccion)



#hen true positive + false positive == 0, precision returns 0 and raises 
#df = pd.read_csv('winequalityred.csv')
#mf,ps,rcs,f1sc,acs,s= Proceso(df, 10, 0.3, 0.20, Proceso.ann()).it()



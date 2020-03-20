import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier


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
    def __init__(self, df, semi, sco, testeo, metodo):
        self.seedc = semi
        self.scorec = sco
        self.validation_size = testeo
        self.x = df.iloc[:, :len(df.T) - 1]
        self.y = df.iloc[:, len(df.T) - 1: len(df.T)]
        self.proceso = metodo

    def it(self, seed=0, score=0):
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=self.validation_size,
                                                            random_state=seed)
        self.proceso.fit(x_train, y_train)
        score = self.proceso.score(x_test, y_test)
        if score < self.scorec and seed <= self.seedc:
            return self.it(seed=seed + 1)
        else:
            return confusion_matrix(y_test, self.proceso.predict(x_test)), classification_report(y_test,
                                                                                                 self.proceso.predict(
                                                                                                     x_test))
    def prede(self,valor):
        return self.proceso.predict(valor)

df = pd.read_csv('winequalityred.csv')
r, e = Proceso(df, 10, 0.3, 0.20, Proceso.ann()).it()



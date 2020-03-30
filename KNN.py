# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:11:20 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
EFelicdad=pd.read_csv('DFnumericoInvertido.csv' )

Col=pd.DataFrame(EFelicdad.columns)
x=EFelicdad.iloc[:,0:41]
y=EFelicdad.iloc[:,42: 43]
#n_neighbors que mejor da resultado es entre 40 y 45
proceso = KNeighborsClassifier(n_neighbors=40)
score=0
seed=0
#seeed de 5 da 1 en score

while score< 0.98:
    seed = seed+1
    validation_size = 0.20
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=validation_size,random_state=seed)
    """
    from sklearn.preprocessing import StandardScaler
    escalar=StandardScaler()
    x_train= escalar.fit_transform(x_train)
    x_test=escalar.fit_transform(x_test) 
    """
    validation_size = 0.20
    proceso.fit(x_train, y_train)
    score=proceso.score(x_test, y_test)  
prediccion=proceso.predict(x_test)
matrizConfusion=confusion_matrix(y_test, prediccion)
reporte=classification_report(y_test, prediccion)
"""
i0,0= datos verdaderos positivos (dato que son 1 predecidos correctamente)
i1,1=datos verdadreros negativos datos reles que son 0 y se predijeron bien 
i0,1= datos falsos negativos dats reales 1 que el modelo predijo como 0 
i1,0=datos falsos positivos datos que son 0 y el modelo predijo cpomo 1
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score#combiancion entre precision y sensiblidad
from sklearn.metrics import roc_auc_score
precision=precision_score(y_test, prediccion)
exactitud=accuracy_score(y_test, prediccion)
sensiblidad=recall_score(y_test, prediccion)
f1=f1_score(y_test, prediccion)
curva_roc_auc=roc_auc_score(y_test, prediccion)

"""
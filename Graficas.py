import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dt={'a':[1,5,4,56,4,45],'b':[1,5,6,6,4,5],'c':[3,5,4,23,4,78],'d':[3,5,5,3,4,4]}
dtdf=pd.DataFrame(dt)
dfdtnp=np.array(dtdf)
def contandoRespuestaPorIntem(matriz):
    vector=[[],[]]
    aux=0
    for i in matriz.columns:
        vector[0].append(matriz[i].value_counts())
        porcentaje=matriz[i].value_counts()/matriz[i].value_counts().sum()
        aux=aux+1
        #plt.pie(porcentaje,labels = porcentaje*100)
        porcentaje.plot.pie(y=i,autopct="%0.1f %%",figsize=(5, 5))
        plt.title(i)
        plt.ylabel('')
        #plt.savefig("imagenP"+str(aux)+".png")
        plt.show()
        vector[1].append(porcentaje)
    return vector

contandoRespuestaPorIntem(dtdf)
def descripcionTemSalida(matriz):
    vector=[]
    for i in matriz.columns:
        vector.append(matriz[i].describe())
    descripcionPoritem=pd.DataFrame(vector).T.replace([None],[0])
    return descripcionPoritem
#DescripcionPorItem1=descripcionTemSalida(dtdf)
#DescripcionPorItem2=descripcionTemSalida(EFelicdad)
def relacionitemsalida(matriz):
    
    vector1=[]
    aux=0
    for i in range(len(matriz)):
        matriz.iloc[i:i+1,:].plot.hist(  )
        plt.xlabel('')
        plt.title(i)
        '''
        matriz.iloc[:,i:i+1].plot.bar(  )
        
        vector1.append(matriz[i])
        #plt.savefig("imagenESta13"+str(aux)+".png")
        aux=aux+1'''
    return vector1

relacionitemSalida29=relacionitemsalida(dtdf)
def graficaHisto(matriz,matriz2):
    aux=0
    for x in matriz.columns:
        
        matriz[x].plot.hist()
        plt.title(x)
        plt.ylabel('')
        plt.xticks(np.arange(2),matriz2[x].drop_duplicates( keep='last'))
        #plt.savefig("imagenH"+str(aux)+".png")
        plt.show()

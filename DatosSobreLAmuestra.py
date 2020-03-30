# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:52:12 2019

@author: (╯°□°)╯︵ ┻━┻
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
EFelicdad=pd.read_csv('DFnumericoInvertido.csv' )
EFelicdadPd=EFelicidad = pd.read_excel('Final_Felicidad_Dicotomizadas(7_11_2019).xlsx',
                                       sheet_name='112 Muestras original').drop(['Marca temporal',
                                    'Dirección de correo electrónico'],axis=1)
EFelicdadPd['clase']=EFelicdad['clase']
EFelicdadPd=EFelicdadPd.replace(["Totalmente en desacuerdo", "Algo en desacuerdo",
                               "Ni en acuerdo ni desacuerdo", "Algo de acuerdo",
                               "Totalmente de acuerdo"],
                                ['TD', 'AD', 'NDT', 'AA', 'TA'])
'''
import seaborn as sb
EFelicdad13Pd=EFelicdad.iloc[:,29:42]

sb.pairplot(EFelicdad, hue='clase',size=7,vars=EFelicdad13Pd,kind='reg')
'''
def contandoRespuestaPorIntem(matriz):
    vector=[[],[]]
    aux=0
    for i in matriz.columns:
        vector[0].append(matriz[i].value_counts())
        porcentaje=matriz[i].value_counts()/matriz[i].value_counts().sum()
        aux=aux+1 
        if aux>29:
            #plt.pie(porcentaje,labels = porcentaje*100)
            porcentaje.plot.pie(y=i,autopct="%0.1f %%",figsize=(5, 5))
            plt.title(i)
            plt.ylabel('')
            #plt.savefig("imagenP"+str(aux)+".png")
            plt.show()
        vector[1].append(porcentaje)
    return vector
def descripcionTemSalida(matriz):
    vector=[]
    for i in matriz.columns:
        vector.append(matriz[i].describe())
    descripcionPoritem=pd.DataFrame(vector).T.replace([None],[0])
    return descripcionPoritem
DescripcionPorItem1=descripcionTemSalida(EFelicdadPd)
DescripcionPorItem2=descripcionTemSalida(EFelicdad)
def relacionitemsalida(matriz):
    vector=[]
    vector1=[]
    aux=0
    for i in EFelicdad.columns:
        if aux<29:
            tabla=pd.crosstab(index=matriz[i],
                                   columns=matriz['clase'], margins=True)
            vector.append(tabla)
            tabla.plot.bar( )
            plt.xlabel('')
            plt.title(i)
            #plt.savefig("imagenESta29"+str(aux)+".png")
        if aux>=29 and aux<42:
            tabla=pd.crosstab(index=matriz[i],
                                   columns=matriz['clase'], margins=True)
            tabla.plot.bar(  )
            plt.xlabel('')
            plt.title(i)
            vector1.append(tabla)
            #plt.savefig("imagenESta13"+str(aux)+".png")
        aux=aux+1
    return vector,vector1
relacionitemSalida29,relacionitemSalida13=relacionitemsalida(EFelicdadPd)
def graficaHisto(matriz,matriz2):
    aux=0
    for x in matriz.columns:
        aux=aux+1 
        if aux>29:
            matriz[x].plot.hist()
            plt.title(x)
            plt.ylabel('')
            plt.xticks(np.arange(2),matriz2[x].drop_duplicates( keep='last'))
            #plt.savefig("imagenH"+str(aux)+".png")
            plt.show()
def calcualrVarPorPregunta(matriz):
    #funcion que calcula la varianza de elemento por elemento
    vector = []
    for i in range(len(matriz.T)):
        vector.append(np.var(matriz[:,i:i+1]))
    vectorNP=np.array(vector)    
    return np.array(vector),vectorNP.sum()
#estadisitca de resumen de los elementos
#en x (media,minimo,maximo,rango,(maximo,minimo), varianza, numero elemntos)
#en y (nedia de los elementos, varianza de los elelemntos, covarianza 
#elementos, correlacionelementos)
def crearEstadisticaDeResumen(medias,varianzas,covarianzas,correralaciones):#, ,):
    vector=[]
    mediasInfo=np.array([medias.mean(),medias.min(),medias.max(),
                         medias.max()-medias.min(),medias.max()/medias.min()
                         ,medias.var(),len(medias)])
    varianzainfo=np.array([varianzas.mean(),varianzas.min(),varianzas.max(),
                         varianzas.max()-varianzas.min(),
                         varianzas.max()/varianzas.min(),varianzas.var(),
                         len(varianzas)])
    covarianzainfo=np.array([covarianzas.mean(),covarianzas.min(),covarianzas.max(),
                         covarianzas.max()-covarianzas.min(),
                         covarianzas.max()/covarianzas.min(),covarianzas.var(),
                         len(covarianzas)])
    correlacionesinfo=np.array([correralaciones.mean(),correralaciones.min(),
                         correralaciones.max(),correralaciones.max()-correralaciones.min(),
                         correralaciones.max()/correralaciones.min(),correralaciones.var(),
                         len(correralaciones)])
    vector.append(mediasInfo.T)
    vector.append(varianzainfo.T)
    vector.append(covarianzainfo)
    vector.append(correlacionesinfo)
    x=['Media','Mínimo','Máximo','rango','Máximo/Mínimo','Varianza','numero de elementos']
    y=['MEdia_elementos','VArainza_elementos','Covarianza elementos','Correlacion_elementos']
    salida=pd.DataFrame(vector,columns=x,index=y)
    return salida

#estadistica de elemto
#organizacon en tabla
#media, desviacionm, tamaño
def calcualrmediaDesvPorEle(matriz):
    vectordesv = []
    vectorMedi=[]  
    for i in range(len(matriz.T)):
        #esto es la media
        media=matriz[:,i:i+1].mean()
        ##esto es la desviacion tipica
        sumatoria=np.array([(x-media)**2 for x in matriz[:,i:i+1] ])
        desviacion=math.sqrt(sumatoria.sum()/len(matriz))
        #va guardadno cada dato de elemento
        vectordesv.append(desviacion)
        vectorMedi.append(media)
        #vector
    vectorNP=np.array(vectordesv)
    vectorNP2=np.array(vectorMedi)    
    return vectorNP2,vectorNP
matrizcovpandas=EFelicdad.cov()
matrizcorrpandas=EFelicdad.corr()
graficaHisto(EFelicdad,EFelicdadPd)
totalesContadosPoritem=contandoRespuestaPorIntem(EFelicdadPd)
npEFelicdad29=np.array(EFelicdad.iloc[:,0:29])
mediaElemento29,desviacionElemento=calcualrmediaDesvPorEle(npEFelicdad29) 
matrizCorrealcion29= np.corrcoef(npEFelicdad29.T)
matrizCovarianza29=np.cov(npEFelicdad29.T)
varPorElemento29,sumVarPorPregunta29=calcualrVarPorPregunta(npEFelicdad29)
resultado29=crearEstadisticaDeResumen(mediaElemento29,varPorElemento29,
                                     matrizCovarianza29,matrizCorrealcion29)
npEFelicdad12=np.array(EFelicdad.iloc[:,29:42])
mediaElemento12,desviacionElemento12=calcualrmediaDesvPorEle(npEFelicdad12) 
matrizCorrealcion12= np.corrcoef(npEFelicdad12.T,ddof=-1)
matrizCovarianza12=np.cov(npEFelicdad12.T)
varPorElemento12,sumVarPorPregunta12=calcualrVarPorPregunta(npEFelicdad12)
resultado12=crearEstadisticaDeResumen(mediaElemento12,varPorElemento12,
                                     matrizCovarianza12,matrizCorrealcion12)
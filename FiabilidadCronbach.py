# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:44:08 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
class FiablidadCronbach:
    def __init__(self):
        
        self.EFelicidad = pd.read_csv('DFnumericoInvertido.csv').drop(['Edad:','Género:','Semestre:',
                                  'Estrato económico:','Estado civil:','Trabaja:',
                                  '¿El nivel de sus ingresos con respecto a sus gastos mensuales son?',
                                  'Promedio académico:','Es creyente','¿Quién costea sus estudios?',
                                  'Tiempo promedio diario de uso del celular:',
                                  '¿En que tipo de casa vive?','clase','Tiempo de traslado'], axis=1)
        matrizEFelicidad=self.EFelicidad.to_numpy().copy()
        totalporpersona,VarT=self.calcularVarTotal(matrizEFelicidad)
        self.indicehomogeneidad=self.corrItemTest(matrizEFelicidad,totalporpersona) 
        self.indicedeCorrelacionT=self.indicecorrelaT(matrizEFelicidad,totalporpersona)
        
        varPorElementoMatrizMejorada,sumVarPorPRegunta=self.calcualrVarPorPregunta(matrizEFelicidad)
        totalporpersona_matrizMEjorVarTMatrizMejo,VarTMAtrizmejorada=self.calcularVarTotal(matrizEFelicidad)
        self.alfa=self.alfaCronbach(matrizEFelicidad,sumVarPorPRegunta,VarTMAtrizmejorada)
        self.siSeRetiraUnElemento=self.matrizCronbacsi(matrizEFelicidad);   
    def resultado(self):
        self.tabla=pd.DataFrame( [self.siSeRetiraUnElemento,
                                                              self.indicehomogeneidad,
                                                              self.indicedeCorrelacionT],
    index=['Alfa sin item',
                                    'Indice homogeneidad',
                                    'Indice homogeneidad c'],
           columns=[x+1 for x in range(len(self.siSeRetiraUnElemento))]).T
        print(self.tabla)
        print('      el alfa de cronbach es: ',self.alfa)
        if self.alfa<0.70:
            print("      Los datos no son consistentes")
        if self.alfa>0.70 and self.alfa<0.80:
            print("      la fiablidad es aceptable")
        if self.alfa>0.80 and self.alfa<0.99:
            print("      la fiablidad es buena")
        if self.alfa==1:
            print("      la fiablidad es exelente")
#funcion de sumatoria de varianza
    def resutadosGrafica(self):
        pass
        #self.grafica=plt.table(self.tabla.to_numpy())
        #https://matplotlib.org/3.1.1/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py
        
    def calcualrVarPorPregunta(self,matriz):
        #funcion que calcula la varianza de elemento por elemento
        vector = []
        for i in range(len(matriz.T)):
            vector.append(np.var(matriz[:,i:i+1]))
        vectorNP=np.array(vector)    
        return np.array(vector),vectorNP.sum()
    #funcion de carianza total
    def calcularVarTotal(self,matriz):
        #funcion que calcula la varianza tota
        vector = []
        for i in range(len(matriz)):
            vector.append(np.sum(matriz[i:i+1,:]))
        vectorNP=np.array(vector)    
        return np.array(vector),np.var(vectorNP)
    def alfaCronbach(self,matriz1,sumVPP,varTotal):
        k=len(matriz1.T)
        alfacrombach=(k/(k-1))*(1-(sumVPP/varTotal))
        return alfacrombach
    def matrizCronbacsi(self,matriz):
        vector=[]
        for i in range(len(matriz.T)):
            matrizSin=np.delete(matriz,[i], axis=1)
            y,sumVarPorPRegunta=self.calcualrVarPorPregunta(matrizSin)
            yy,VarT=self.calcularVarTotal(matrizSin)
            #esto es la formula de alfa cronbach
            k=len(matrizSin.T)
            alfaCrombach=(k/(k-1))*(1-(sumVarPorPRegunta/VarT))
            #va guardadno cada dato de elemento
            vector.append(alfaCrombach)
        return np.array(vector)
    #indice de homogeneidad
    def corrItemTest(self,matriz1,totalpersoa):
        salida=[]
        for x in range(len(matriz1.T)):
            b=totalpersoa
            a=matriz1[:,x:x+1].reshape(len(matriz1),)
            c=np.corrcoef(a,b)[0,1]
            salida.append(c)
        return np.array(salida)
    ####mejorar crombacha########################################################################
    def indicecorrelaT(self,matriz1,totalpersoa):
        salida=[]
        
        for x in range(len(matriz1.T)):
            b=totalpersoa
            a=matriz1[:,x:x+1].reshape(len(matriz1),)
            c=np.corrcoef(a,b-a)[0,1]
            salida.append(c)
        return np.array(salida)

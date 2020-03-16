# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
import numpy as np
import math
dt={'a':[1,5,4,56,4,45],'b':[1,5,6,6,4,5],'c':[3,5,4,23,4,78],'d':[3,5,5,3,4,4]}
dtdf=pd.DataFrame(dt)
dfdtnp=np.array(dtdf)
class Estadis():
    def __init__(self,df):
        self.dtdf=pd.DataFrame(df)
        self.dfdtnp=np.array(dtdf)
        self.__x=['Media','Mínimo','Máximo','rango','Máximo/Mínimo','Varianza','numero de elementos']
        self.__y=['MEdia_elementos','VArainza_elementos','Covarianza elementos','Correlacion_elementos']
        self.__vector=[]
        self.inf=pd.DataFrame(np.zeros((4,7)),columns=self.__x,index=self.__y)
    
    def varPorItem(self):
        return np.array([np.var(self.dtdf.iloc[:,i:i+1]) for i in range(len(self.dtdf.T))]).reshape(len(self.dtdf.T),),np.array([np.var(self.dtdf.iloc[:,i:i+1]) for i in range(len(self.dtdf.T))]).reshape(len(self.dtdf.T),).sum

    def calcularVarPorRegistro(self):
        return np.array([np.sum(self.dfdtnp[i:i+1,:]) for i in range(len(self.dfdtnp))]),np.var([np.sum(self.dfdtnp[i:i+1,:]) for i in range(len(self.dfdtnp))])
    #totalPersona2,varTpersona2=calcularVarPorRegistro(dfdtnp)
    
    
    def corrIteTest(self):
        return np.array([np.corrcoef(self.dfdtnp[:,x:x+1].reshape(len(self.dfdtnp),),self.calcularVarPorRegistro()[0])[0,1] for x in range(len(self.dfdtnp.T))])
    #indiceHomogeneidad=corrIteTest(dfdtnp,totalPersona2)
    
    def correIteTestCorreg(self):
        return np.array([np.corrcoef(self.dfdtnp[:,x:x+1].reshape(len(self.dfdtnp),),self.calcularVarPorRegistro()[0]-self.dfdtnp[:,x:x+1].reshape(len(self.dfdtnp),))[0,1] for x in range(len(self.dfdtnp.T))])
    #indicedeCorrelacionCorregi=correIteTestCorreg(dfdtnp,totalPersona2)
    
    def calculardesviacion(self):
        return np.array([math.sqrt(np.array([(x-self.dfdtnp[:,i:i+1].mean())**2 for x in self.dfdtnp[:,i:i+1] ]).sum()/len(self.dfdtnp)) for i in range(len(self.dfdtnp.T))])
    def calcularVarianza(self):
        return np.array([np.array([(x-self.dfdtnp[:,i:i+1].mean())**2 for x in self.dfdtnp[:,i:i+1] ]).sum()/len(self.dfdtnp) for i in range(len(self.dfdtnp.T))])
    
    def calcularMedia(self):
        return np.array([self.dfdtnp[:,i:i+1].mean() for i in range(len(self.dfdtnp.T))])
    
    def calcularCovarianza(self):
        return np.cov(self.dfdtnp.T)
    def calcularCorrela(self):
        return np.corrcoef(self.dfdtnp.T)
    def descripcionPd(self):
        return pd.DataFrame([self.dfdtnp[i].describe() for i in self.dfdtnp.columns]).T
    def __resuMed(self):
        
        self.__vector.append(np.array([self.calcularMedia().mean(),self.calcularMedia().min(),self.calcularMedia().max(),
                         self.calcularMedia().max()-self.calcularMedia().min(),self.calcularMedia().max()/self.calcularMedia().min()
                         ,self.calcularMedia().var(),len(self.calcularMedia())]).T)
    def __resuvar(self):
        self.__vector.append(np.array([self.calcularVarianza().mean(),self.calcularVarianza().min(),self.calcularVarianza().max(),
                         self.calcularVarianza().max()-self.calcularVarianza().min(),
                         self.calcularVarianza().max()/self.calcularVarianza().min(),self.calcularVarianza().var(),
                         len(self.calcularVarianza())]).T)
    def __resucova(self):
        self.__vector.append(np.array([self.calcularCovarianza().mean(),self.calcularCovarianza().min(),self.calcularCovarianza().max(),
                         self.calcularCovarianza().max()-self.calcularCovarianza().min(),
                         self.calcularCovarianza().max()/self.calcularCovarianza().min(),self.calcularCovarianza().var(),
                         len(self.calcularCovarianza())]).T)
    def __resuCorre(self):
        self.__vector.append(np.array([self.calcularCorrela().mean(),self.calcularCorrela().min(),
                         self.calcularCorrela().max(),self.calcularCorrela().max()-self.calcularCorrela().min(),
                         self.calcularCorrela().max()/self.calcularCorrela().min(),self.calcularCorrela().var(),
                         len(self.calcularCorrela())]).T)
    
    def mostrarResumen(self):
        self.__resuMed()
        self.__resuvar()
        self.__resucova()
        self.__resuCorre()
        return pd.DataFrame(self.__vector,columns=self.__x,index=self.__y)

p=Estadis(dt).varPorItem()[0]
p1=Estadis(dt).calcularVarPorRegistro()[0]
p2=Estadis(dt).corrIteTest()
p3=Estadis(dt).correIteTestCorreg()
p4=Estadis(dt).calculardesviacion()
p5=Estadis(dt).calcularVarianza()
p7=Estadis(dt).calcularCovarianza()
p8=Estadis(dt).calcularCorrela()
p6=Estadis(dt).calcularMedia()
p10=Estadis(dt).mostrarResumen()

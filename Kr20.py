# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:30:25 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np
class Kr20:
    def __init__(self):
        self.EFelicdad=pd.read_csv('DFnumericoInvertido.csv' )
        self.seleccion=self.EFelicdad.iloc[:,29:42]
        self.seleccion['total']=self.seleccion.sum(axis=1)
        self.result=self.kr20(self.seleccion)        
        self.rCorrItemTest=self.corrItemTest(self.seleccion)
        self.rIndiceHCorregido=self.indicecorrelaT(self.seleccion)
        self.siseQuitaElemento=self.siSequitaElemento(self.seleccion)
    def kr20(self,seleccion):
        p=seleccion.drop(['total'], axis =1).mean(axis=0)
        q=1-p
        pq=p*q
        k=len(seleccion.T)-1
        
        sumatoria_pq=pq.sum()
        varT=seleccion['total'].var(ddof=0)
        result=(k/(k-1))*(1-(sumatoria_pq/varT))
        return result
    def siSequitaElemento(self,seleccion):
        vector=[]
        
        for x in seleccion.drop(['total'],axis =1).columns:
            
            seleccionBorrar=seleccion.drop([x],axis =1).copy()
            p=seleccionBorrar.drop(['total'],axis =1).mean(axis=0)
            q=1-p
            pq=p*q
            k=len(seleccionBorrar.T)-1
            sumatoria_pq=pq.sum()
            
            varT=seleccionBorrar['total'].var(ddof=0)
            result=(k/(k-1))*(1-(sumatoria_pq/varT))
            
            vector.append(result)
        return vector
    def resultado(self):
         self.tabla=pd.DataFrame( [self.siseQuitaElemento,
                                                              self.rCorrItemTest,
                                                              self.rIndiceHCorregido],
    index=['kr20 sin el item',
                                    'Indice homogeneidad',
                                    'Indice homogeneidad c'],
           columns=[x+1 for x in range(len(self.siseQuitaElemento))]).T
         print(self.tabla)
         
         print('      el indice de kr20 es: ',self.result)
         if self.result<0.70:
             print("      Los datos no son consistentes")
         if self.result>0.70 and self.result<0.80:
             print("      la fiablidad es aceptable")
         if self.result>0.80 and self.result<0.99:
             print("      la fiablidad es buena")
         if self.result==1:
             print("      la fiablidad es exelente")
    
    def corrItemTest(self,matriz1):
        salida=[]
        for x in matriz1.drop(['total'], axis =1):
            b=matriz1['total']
            a=matriz1[x]
            c=np.corrcoef(a,b)[0,1]
            salida.append(c)
        return salida
    
    def indicecorrelaT(self,matriz1):
        salida=[]
        for x in matriz1.drop(['total'], axis =1):
            b=matriz1['total']
            a=matriz1[x]
            c=np.corrcoef(a,b-a)[0,1]
            salida.append(c)
        return salida
    
    """vector=[]
    for i in seleccion.drop(['total'], axis =1):
        vector.append( seleccion[i][seleccion[i]==1].value_counts()/len(seleccion))
    p=pd.DataFrame(vector).T
    resul2t=(k/(k-1))*((varT-sumatoria_pq)/varT)
    """
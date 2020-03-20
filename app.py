import csv
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from numpy.core._multiarray_umath import ndarray
import ML
import Estadistica
import Arreglar

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html', methods=['GET', 'POST'])
def rindex():
    if request.method == 'POST':
        return render_template('index.html')


@app.route('/Visualizacion.html', methods=['GET', 'POST'])
def data():
    try:
        df = pd.DataFrame(request.files['files'])
        df.to_csv('pruebaas.csv', index=False)
        dfc = pd.read_csv('pruebaas.csv', sep=',', header=None)
        cv = Arreglar.arre(df).reparaCSV()
        print(type(cv['fixedacidity'][0]))
        Estadistica.Estadis(cv)
        p = pd.DataFrame(Estadistica.Estadis(cv).varPorItem().T, columns=cv.columns, index=['Varianza'])
        print(p)
        p1 = Estadistica.Estadis(cv).calcularVarPorRegistro()
        p2: ndarray = Estadistica.Estadis(cv).corrIteTest()
        p3 = Estadistica.Estadis(cv).correIteTestCorreg()
        p4 = Estadistica.Estadis(cv).calculardesviacion()
        p5 = Estadistica.Estadis(cv).calcularVarianza()
        p7 = Estadistica.Estadis(cv).calcularCovarianza()
        p8 = Estadistica.Estadis(cv).calcularCorrela()
        p6 = Estadistica.Estadis(cv).calcularMedia()
        p9 = Estadistica.Estadis(cv).mostrarResumen()
        print(p2)
        print(p3)
        print(p9)

        return render_template('Visualizacion.html', tables=[p.to_html(classes='data', header="true")],
                               tables1=[pd.DataFrame(p2.T, index=cv.columns, columns=['IH']).to_html(classes='data',
                                                                                                     header="true")],
                               tables2=[pd.DataFrame(p3.T, index=cv.columns, columns=['IHC']).to_html(classes='data',
                                                                                                      header="true")],
                               tables3=[pd.DataFrame(p8.T, index=cv.columns, columns=cv.columns).to_html(classes='data',
                                                                                                         header="true")],
                               tables4=[pd.DataFrame(p9).to_html(classes='data', header="true")],
                               data=cv.to_html())
    except:
        dfc = pd.read_csv('pruebaas.csv', sep=',', header=None)
        cv = Arreglar.arre(dfc).reparaCSV()

        Estadistica.Estadis(cv)
        p = pd.DataFrame(Estadistica.Estadis(cv).varPorItem().T, columns=cv.columns, index=['Varianza'])

        Estadistica.Estadis(cv).calcularVarPorRegistro()
        p2: ndarray = Estadistica.Estadis(cv).corrIteTest()
        p3 = Estadistica.Estadis(cv).correIteTestCorreg()
        Estadistica.Estadis(cv).calculardesviacion()
        Estadistica.Estadis(cv).calcularVarianza()
        Estadistica.Estadis(cv).calcularCovarianza()
        p8 = Estadistica.Estadis(cv).calcularCorrela()
        Estadistica.Estadis(cv).calcularMedia()
        p9 = Estadistica.Estadis(cv).mostrarResumen()
        return render_template('Visualizacion.html', tables=[p.to_html(classes='data', header="true")],
                               tables1=[pd.DataFrame(p2.T, index=cv.columns, columns=['IH']).to_html(classes='data',
                                                                                                     header="true")],
                               tables2=[pd.DataFrame(p3.T, index=cv.columns, columns=['IHC']).to_html(classes='data',
                                                                                                      header="true")],
                               tables3=[pd.DataFrame(p8.T, index=cv.columns, columns=cv.columns).to_html(classes='data',
                                                                                                         header="true")],
                               tables4=[pd.DataFrame(p9).to_html(classes='data', header="true")],
                               data=cv.to_html())


@app.route('/ML.html', methods=['GET', 'POST'])
def ml():
    if request.method == 'POST':
        r=pd.DataFrame(np.zeros((3,5)))
        dfc = pd.read_csv('pruebaas.csv', sep=',', header=None)
        cv = Arreglar.arre(dfc).reparaCSV()
        sem=request.args.get('semilla') 
        sem=request.args.get('pres') 
        sem=request.args.get('tes') 
        if request.form.get('ann'):
            r, e = ML.Proceso(cv, 10, 0.3, 0.20, ML.Proceso.ann()).it()
        if request.form.get('knn'):
            r, e = ML.Proceso(cv, 10, 0.3, 0.20, ML.Proceso.ann()).it()
        if request.form.get('svc'):
            r, e = ML.Proceso(cv, 10, 0.3, 0.20, ML.Proceso.ann()).it()
        if request.form.get('lg'):
            r, e = ML.Proceso(cv, 10, 0.3, 0.20, ML.Proceso.ann()).it()                
        return render_template('ML.html',data=pd.DataFrame(r).to_html())


@app.route('/InfoData')
def infodata():
    return 'info data'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

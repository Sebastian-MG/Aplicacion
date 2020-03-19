import csv
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import math
import csv
import os
import Estadistica
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/data',methods=['POST'])
def data():
    if request.method == 'POST':
        df = pd.DataFrame(request.files['files'])
        for i in range(len(df)):
            f = str(df.iloc[i:i + 1, :])
            if i>=1:

                f=f.replace('\"', '')
                f = f.replace('\'', '')
                f = f.replace('b', '')
                f= f.replace('\\', '')#\r\n'"
                f = f.replace('r', '')
            else:
                nombres=f


            print(f)

        df.to_csv('pruebaas.csv', index=False)

        return 'hola'#render_template('visualizacion.html', data=df.to_html())
@app.route('/InfoData')
def infodata():
    return 'info data'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

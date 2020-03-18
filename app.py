import csv
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import math
import csv
import Estadistica
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload.html', methods=['POST'])
def upload_route_summary():
    if request.method == 'POST':
        # Create variable for uploaded file
        f = request.files['fileupload']

        # store the file contents as a string
        fstring = f.read()

        # create list of dictionaries keyed by header row
        csv_dicts = [{k: v for k, v in row.items()} for row in
                     csv.DictReader(fstring.splitlines(), skipinitialspace=True)]

        # do something list of dictionaries
    return "success"

@app.route('/data',methods=['POST'])
def data():
    if request.method == 'POST':
        df = pd.DataFrame(request.files['files'])
        f = request.files["files"]
        print(type(f))
        fstring = f.read()
        csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(fstring.splitlines(), skipinitialspace=True)]
        df=pd.DataFrame(csv_dicts)


        df.to_csv('pruebaas.csv', index=False, sep=',')

        return 'hola'#render_template('visualizacion.html', data=df.to_html())
@app.route('/InfoData')
def infodata():
    return 'info data'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

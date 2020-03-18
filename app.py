import csv
from flask import Flask, render_template, request
import pandas as pd
import Estadistica as es
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data',methods=['POST'])
def data():
    if request.method == 'POST':
        df = pd.DataFrame(request.files['files'])
        cs=csv.reader(request.files['files'])
        return str(str(cs))

@app.route('/InfoData')
def infodata():
    return 'info data'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

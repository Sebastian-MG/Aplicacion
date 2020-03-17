from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data',methods=['POST'])
def data():
    if request.method == 'POST':
        archivoCSV = pd.DataFrame(request.form['index.html'])
        return 'llego el archivo'

@app.route('/InfoData')
def infodata():
    return 'info data'


if __name__ == '__main__':
    app.run(port=5000, debug=True)

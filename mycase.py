import random
import datetime

from flask import Flask, render_template,jsonify,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ptime')
def get():
    str1=datetime.datetime.today()
    str2=str1.strftime("%Y-%m-%d %X")
    return str2


if __name__ == '__main__':
    app.run(debug=True)
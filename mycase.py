import random
import datetime

from flask import Flask, render_template,jsonify,url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

#打开test.html页面，运行本python程序后在本地浏览器输入http://127.0.0.1:5000/test即可打开	
@app.route('/test')
def test():
	return render_template('test.html')
	
#打开drawtest.html页面，运行本python程序后在本地浏览器输入http://127.0.0.1:5000/drawtest即可打开	
@app.route('/drawtest')
def drawtest():
	return render_template('drawtest.html')


@app.route('/ptime')
def get():
    str1=datetime.datetime.today()
    str2=str1.strftime("%Y-%m-%d %X")
    return str2
	
@app.route('/settext')	
def settext():
	return "ajax从flask传参测试"

@app.route('/datafig1',methods=["GET","POST"])
def setdata1():
    data1={}
    data1["TimeList"]=["2017-01","2017-02","2017-03","2017-04","2017-05","2017-06","2017-07","2017-08","2017-09"]
    data1["lv1"]=[1000,1200,3000,2000,1200,2500,2600,1400,2200]
    data1['lv2']=[200,250,300,120,158,460,220,230,600,110]
    data1['lv3']=[20,40,22,35,16,80,100,26,30]
    data1['lv4']=[20,40,22,35,16,80,100,26,30]
    # data1={}
    # data1["md"]=1
    # data1["mb"]=2
    return jsonify(data1)



if __name__ == '__main__':
    app.run(debug=True)
import sqlite3
from flask import Flask,render_template,request,session,g,redirect,url_for,\
    abort,flash
from wxTools import wxTools


app = Flask(__name__)
app.secret_key='test'

@app.route('/')
def hello_world():
    totalvistor=1234
    todayvistor=23
    return render_template('index.html',totalvistor=totalvistor,todayvistor=todayvistor)

@app.route('/test')
def test():
    return render_template('newsmessage.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
# @app.route('/wx',methods=['GET','POST'])
# def wxfun():
#     if request.method=='GET':
#         print request.args.get('signature','null')

if __name__ == '__main__':
    app.run(debug=True)

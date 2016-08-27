from flask import Flask,render_template,request
from wxTools import wxTools

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',messagenum=100,newusers=135,totalusers=10003)

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

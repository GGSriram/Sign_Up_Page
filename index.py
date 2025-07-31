from flask import Flask, render_template

from markupsafe import escape
app=Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/hello')
def hhhj():
    items = [
        {'id':1,'name':'Phone','barcode':'123456789012345','price':500},
        {'id':2,'name':'Laptop','barcode':'098765432109876','price':1000},
        {'id':3,'name':'Keyboard','barcode':'345658034567992','price':800}
    ]
    return render_template('index.html', items=items)

@app.route('/user/<username>')
def show(username):
    return f'Hello {escape(username)}'
app.run(debug=True,port=8080)
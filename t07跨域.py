from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('tmp01.html')

@app.route('/index2')
def index2():
    return 'index2'


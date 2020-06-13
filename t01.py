from flask import Flask
from flask import render_template

# 1.实例化Flask类, __name__是文件名
app = Flask(__name__, static_url_path='/my_static')

@app.route('/')
def index():
    # return __name__
    return render_template('tmp01.html')
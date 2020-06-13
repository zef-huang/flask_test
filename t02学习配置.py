from flask import Flask
from flask import render_template

# 1.实例化Flask类, __name__是文件名
app = Flask(__name__, static_url_path='/my_static')

# 1.配置类
# class Config():
#     REDIS = "redis://127.0.0.1/1"
# app.config.from_object(Config)

# 2.配置文件
# app.config.from_pyfile('config.ini')

# 3.环境变量
# app.config.from_envvar('CONFIG')

# print(app.config.get("REDIS"))

# 视图函数
@app.route('/')
def index():
    # return __name__
    return render_template('tmp01.html')
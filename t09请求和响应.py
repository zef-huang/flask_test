from flask import Flask, make_response

app = Flask(__name__)

##############################################
# url字符串获取参数和转化器
# @app.route('/<int:user_id>')
# def user_index(user_id):
#     return "user_id is {}".format(user_id)

# 转换器的两个作用: 1.转换类型, 2.过滤无效url
##############################################
# 来, 自定义个转换器
from werkzeug.routing import BaseConverter
class MobileConverter(BaseConverter):
    regex = '1[3-9]\d{9}'

app.url_map.converters['mobile'] = MobileConverter

@app.route("/<mobile:phone_number>")
def index(phone_number):
    return "phone number is {}".format(phone_number)

##############################################
# 获取request参数
from flask import request

@app.route('/request', methods=['POST', 'GET'])
def req():
    print(request.args)
    print(request.form.get("life"))
    photo = (request.files.get("photo"))
    photo.save("photo.jpg")
    return "OK"


##############################################
# 返回响应
@app.route("/response")
def resp():
    response = make_response("response")
    response.status_code = 301
    response.headers = {"token":"struggle"}
    return response

# 返回json
from flask import jsonify
@app.route("/json")
def json_resp():
    data = {"wheather":"rain", "mood":"sad"}
    return jsonify(data="data", age="age")


# 返回jinja2
from flask import render_template

@app.route('/jinja')
def jinja():
    return render_template("tmp01.html", name="sad")

# 设置cookie
@app.route("/cookie")
def set_cookie():
    response = make_response("设置成功")
    response.set_cookie("session_id","sdghgkshgdsdgl")
    return response

# 查询cookie
@app.route("/require_cookie")
def require_cookie():
    sid = request.cookies.get("session_id")
    return sid

# 删除cookie
@app.route("/delete_cookie")
def delete_cookie():
    response = make_response("删除成功")
    response.delete_cookie("session_id")
    return response


from flask import session
app.secret_key = "hzf"

@app.route('/session')
def set_session():
    session['name'] = 'huangzefeng'
    return "设置session成功"

# 查看session
@app.route('/get_session')
def get_session():
    name = session.get('name')
    return name

#删除session
@app.route('/delete_session')
def delete_session():
    session.pop('name')
    return "删除成功"

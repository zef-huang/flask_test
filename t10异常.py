from flask import Flask, abort

app = Flask(__name__)

@app.route("/<string:crazy>")
def accident(crazy):
    abort(404, "crazy things happend")

# 创建特定错误页面
@app.errorhandler(404)
def err404(e):
    return "<h1>访问发生错误</h1>"

# 函数注释
def add(x:12,y:13) ->accident:
    return x+y


def f(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
    print("函数注释", f.__annotations__)
    print("参数值打印", ham, eggs)
    print(type(ham), type(eggs))


print(add(1,2.0))
print(type(add(1.2, 2)))
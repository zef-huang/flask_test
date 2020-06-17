from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data = {}
    url_iteror = app.url_map.iter_rules()
    for url in url_iteror:
        data[url.endpoint] = url.rule
    return jsonify(data)


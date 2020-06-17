from flask import Flask, Blueprint

from user import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)


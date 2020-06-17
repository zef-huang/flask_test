from . import user_bp
from flask import render_template

@user_bp.route('/')
def user():
    # return "user_bp"
    return render_template('user.html')
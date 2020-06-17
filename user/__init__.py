from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user',
                    static_url_path='/user_static', static_folder='user_static',
                    template_folder='user_templates')

from . import view
from flask import Blueprint

teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

from app.teachers import route
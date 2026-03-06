from flask import Blueprint

dashboard_bp = Blueprint(
    "dashboard",   # ⚠️ ce nom est important
    __name__,
    template_folder="templates"
)

from . import route
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
from ..models import Permission
from .. import mongo
 

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

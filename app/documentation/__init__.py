from flask import Blueprint

admin_docs = Blueprint('documentation', __name__, template_folder='templates')

from . import routes

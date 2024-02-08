import logging

from flask import abort, render_template, redirect, url_for, request, current_app
from flask_login import current_user

from . import public_bp


logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info('Mostrando los posts del blog')
    return render_template("public/index.html")


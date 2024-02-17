from flask import Flask, jsonify, render_template
from flask_restful import Api
from flask_login import LoginManager

from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.films.api_v1_0.resources import films_v1_0_bp

from .ext import ma, migrate
from app.common.filters import format_datetime


login_manager = LoginManager()


def create_app(settings_module):
    app = Flask(__name__)
    app.secret_key = "super secret string" 
    app.config.from_object(settings_module)
    app.debug = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    
    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Captura todos los errores 404
    Api(app, catch_all_404s=True)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

    # Registra los blueprints
    app.register_blueprint(films_v1_0_bp)
    
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from app.admin import admin_bp
    app.register_blueprint(admin_bp)
    
    from app.public import public_bp
    app.register_blueprint(public_bp)
    
    from app.documentation import admin_docs
    app.register_blueprint(admin_docs)
    
    # Registra manejadores de errores personalizados
    register_error_handlers(app)

    return app

def register_filters(app):
    app.jinja_env.filters['datetime'] = format_datetime
    

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': f'Internal server error {e}'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': f'Method not allowed {e}'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': f'Forbidden error {e}'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': f'Not Found error {e}'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
    
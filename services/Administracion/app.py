import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from src.core.config import Parametros
from src.restaurantes.routes import restaurantes_bp
from src.sucursales.routes import sucursales_bp
from src.mesas.routes import mesas_bp
from src.horarios.routes import horarios_bp
from src.promociones.routes import promociones_bp
from src.core.logs import HandleLogs



def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__, static_folder='static')

    # CORS configuration
    CORS(app, origins=Parametros.cors_origins, supports_credentials=True)

    # Register blueprints with /api/admin prefix
    app.register_blueprint(restaurantes_bp, url_prefix='/restaurantes')
    app.register_blueprint(sucursales_bp, url_prefix='/sucursales')
    app.register_blueprint(mesas_bp, url_prefix='/mesas')
    app.register_blueprint(horarios_bp, url_prefix='/horarios')
    app.register_blueprint(promociones_bp, url_prefix='/promociones')
    app.register_blueprint(
        get_swaggerui_blueprint(
            '/docs',
            '/static/swagger.json',
            config={
                'app_name': "MS Admin - Documentación Swagger"
            }
        )
        , url_prefix='/docs')

    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "healthy", "service": "ms-admin"}), 200

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "message": "Recurso no encontrado"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"success": False, "message": "Error interno del servidor"}), 500

    return app


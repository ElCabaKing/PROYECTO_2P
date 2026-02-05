from flask import jsonify
import logging
from core.exceptions import AppError
from marshmallow import ValidationError
from core.exceptions import UnauthorizedError
from itsdangerous import SignatureExpired, BadSignature, BadTimeSignature
from psycopg2.errors import UniqueViolation

logger = logging.getLogger(__name__)

def register_error_handlers(app):

    @app.errorhandler(AppError)
    def handle_app_error(error):
        logger.warning(error.message)
        return jsonify({"error": error.message}), error.status_code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        logger.exception("Error inesperado")
        return jsonify({"error": "Error interno del servidor"}), 500

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        logger.warning("Error de validación: %s", error.messages)
        return jsonify({
            "error": "Datos inválidos",
            "details": error.messages
        }), 422
    
    @app.errorhandler(UnauthorizedError)
    def handle_unauthorized_error(error):
        logger.warning("Error de autorización: %s", error.message)
        return jsonify({"error": error.message}), 401
    
        
    @app.errorhandler(SignatureExpired)
    def handle_signature_expired(error):
        logger.warning("Token expirado: %s", str(error))
        return jsonify({"error": "Token expirado"}), 410
    
    
    @app.errorhandler(BadSignature)
    def handle_bad_signature(error):
        logger.warning("Firma inválida: %s", str(error))
        return jsonify({"error": "Token inválido"}), 400
    
    @app.errorhandler(BadTimeSignature)
    def handle_bad_time_signature(error):
        logger.warning("Firma temporal inválida: %s", str(error))
        return jsonify({"error": "Token expirado o inválido"}), 400
    
        
    @app.errorhandler(UniqueViolation)
    def handle_unique_violation(error):
        logger.warning("Violación de unicidad: %s", str(error))
        return jsonify({"error": "El registro ya existe"}), 400
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from core.error_handler import register_error_handlers
import os
from core.logs import setup_logger
from src.extensions.mailInit import mail
from src.config.email import Config




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    CORS(app, origins="localhost:3000")  # Configurar CORS para permitir solicitudes desde localhost:3000

    setup_logger()
    register_error_handlers(app)
    # Swagger config
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Api Seguridad"
        }
    )   
    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config["JWT_ACCESS_COOKIE_NAME"] = "access_token"
    app.config["JWT_COOKIE_CSRF_PROTECT"] = False

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    


    from src.modules.user.routes import user_bp
    app.register_blueprint(user_bp)
    from src.modules.auth.routes import auth_bp
    app.register_blueprint(auth_bp)
    
    return app

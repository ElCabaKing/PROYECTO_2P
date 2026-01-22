from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint



def create_app():

    app = Flask(__name__)
    
    # Swagger config
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Mi API Flask"
        }
    )   

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    

#como agregar rutas :3
#    from src.routes.user_route import user_bp
#   app.register_blueprint(user_bp, url_prefix="/api/users")

    return app

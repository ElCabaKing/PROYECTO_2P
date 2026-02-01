from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint



def create_app():

    app = Flask(__name__)
    CORS(app)
    
    # Swagger config
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Reserva"
        }
    )   

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app

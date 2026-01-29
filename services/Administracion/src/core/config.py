import configparser
import os

path = os.path.abspath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(path, 'config.cfg'))


class Parametros:
    # Database
    db_host = os.getenv('DB_HOST', config.get('database', 'host'))
    db_port = os.getenv('DB_PORT', config.get('database', 'port'))
    db_user = os.getenv('DB_USER', config.get('database', 'user'))
    db_pass = os.getenv('DB_PASSWORD', config.get('database', 'password'))
    db_name = os.getenv('DB_NAME', config.get('database', 'name'))

    # JWT
    secret_key = os.getenv('SECRET_KEY', config.get('jwt', 'secret_key'))
    algorithm = os.getenv('ALGORITHM', config.get('jwt', 'algorithm'))

    # CORS
    cors_origins = os.getenv(
        'CORS_ORIGINS',
        config.get('cors', 'origins')
    ).split(',')

    # Services
    security_url = os.getenv('SECURITY_SERVICE_URL', config.get('services', 'security_url'))


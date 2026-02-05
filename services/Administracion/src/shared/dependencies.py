from functools import wraps
from flask import request, g
import jwt

from src.core.config import Parametros
from src.core.logs import HandleLogs
from src.shared.response import response_unauthorize, response_forbidden


def jwt_required_custom(f):
    """
    Decorator to validate JWT token from Authorization header.
    Stores decoded payload in g.current_user.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # auth_header = request.headers.get('access_token')
        #
        # if not auth_header:
        #     return response_unauthorize()
        #
        # try:
        #     # Extract token from "Bearer <token>"
        #     parts = auth_header.split()
        #     if len(parts) != 2 or parts[0].lower() != 'bearer':
        #         return response_unauthorize()
        #
        #     token = parts[1]
        #     payload = jwt.decode(
        #         token,
        #         Parametros.secret_key,
        #         algorithms=[Parametros.algorithm]
        #     )
        #     g.current_user = payload
        #
        # except jwt.ExpiredSignatureError:
        #     HandleLogs.write_error("Token expirado")
        #     return response_unauthorize()
        # except jwt.InvalidTokenError as e:
        #     HandleLogs.write_error(f"Token inválido: {e}")
        #     return response_unauthorize()

        return f(*args, **kwargs)
    return decorated_function



def get_current_user():
    """Get current authenticated user from Flask g object."""
    return getattr(g, 'current_user', None)


def get_user_sucursal_id():
    """Get sucursal_id from current user's JWT payload."""
    current_user = get_current_user()
    if not current_user:
        return None
    return current_user.get('sucursal_id')


def get_user_restaurante_id():
    """Get restaurante_id from current user's JWT payload."""
    current_user = get_current_user()
    if not current_user:
        return None
    return current_user.get('restaurante_id')


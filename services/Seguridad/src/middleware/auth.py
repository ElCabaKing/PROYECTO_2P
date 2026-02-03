from functools import wraps
from flask import g
from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt,
    get_jwt_identity,
    exceptions
)
from core.exceptions import UnauthorizedError

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request(locations=["cookies"])
        except exceptions.NoAuthorizationError:
            raise UnauthorizedError("Token no proporcionado")
        except exceptions.JWTExtendedException:
            raise UnauthorizedError("Token inválido")

        claims = get_jwt()
        g.user_cid = get_jwt_identity()
        g.sucursal_id = claims.get("sucursal_id")
        g.restaurant_id = claims.get("restaurant_id")
        print(g.sucursal_id, g.restaurant_id)
        g.role = claims.get("role")
        g.user_id = claims.get("user_id")
        print(claims)

        if g.sucursal_id is None and g.restaurant_id is None:
            raise UnauthorizedError("Token mal formado")

        return f(*args, **kwargs)

    return decorated


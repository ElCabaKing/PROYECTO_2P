class AppError(Exception):
        message = "Error en el servidor"
        status_code = 500
        
        def __init__(self, message):
            self.message = message
        
class NotFoundError(AppError):
    status_code = 404
    message = "Recurso no encontrado"

class BadRequestError(AppError):
    status_code = 400
    message = "Solicitud incorrecta"

class UnauthorizedError(AppError):
    status_code = 401
    message = "No autorizado"

class ForbiddenError(AppError):
    status_code = 403
    message = "Acceso denegado"
    
class ValidationError(AppError):
    status_code = 422
    message = "Error de validación"
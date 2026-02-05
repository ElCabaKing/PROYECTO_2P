from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import os
serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))

salt = "recovery-password"

def generar_token(id):
    return serializer.dumps(id, salt=salt)


def validate_recovery_token(token, max_age=1*60*60*4):
        data = serializer.loads(token, max_age=max_age, salt=salt)
        return data

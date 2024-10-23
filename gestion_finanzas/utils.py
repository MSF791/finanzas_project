import jwt
import datetime
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

# Generar un token JWT
def generate_jwt_token(user):
    payload = {
        'id': user.id,
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email,
        'telefono':user.telefono,
        'password':user.password,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)  
        
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

# Verificar un token JWT
def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except ExpiredSignatureError:
        raise ExpiredSignatureError("El token ha expirado")
    except InvalidTokenError:
        raise InvalidTokenError("El token es inválido")
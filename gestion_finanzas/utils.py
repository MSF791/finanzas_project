import jwt
import datetime
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from django.core.mail import EmailMessage

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
    
def enviar_mensaje(email, factura):
    asunto='Recordatorio Pago Factura'
    mensaje=f'Recuerda que te quedan dos dias para pagar la factura: \n {factura["nombre"]}, \n para la fecha: {factura["fecha"]} \n con un valor de: {factura["cantidad"]}'
    remitente = 'modasinfronteras2@gmail.com'
    destinatarios = [email]
    correo = EmailMessage(asunto, mensaje, remitente, destinatarios)
    try:
        correo.send()
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    return 
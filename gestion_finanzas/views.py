from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .utils import generate_jwt_token, decode_jwt_token
from .serializer import *
from .models import *
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class IngresoView(viewsets.ModelViewSet):
    serializer_class = IngresoSerializer
    queryset = Ingreso.objects.all()

class GastoView(viewsets.ModelViewSet):
    serializer_class = GastoSerializer
    queryset = Gasto.objects.all()

class ObjetivoAhorroView(viewsets.ModelViewSet):
    serializer_class = ObjetivoAhorroSerializer
    queryset = ObjetivoAhorro.objects.all()

class PresupuestoView(viewsets.ModelViewSet):
    serializer_class = PresupuestoSerializer
    queryset = Presupuesto.objects.all()

class FacturaView(viewsets.ModelViewSet):
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()

class ObtainJwtToken(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = Usuario.objects.get(username=username, password=password)
            token = generate_jwt_token(user)
            return Response({'token': token}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error':'Credenciales no válidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LoadJwtToken(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            res = decode_jwt_token(token)
            return Response({'respuesta':res}, status=status.HTTP_200_OK)
        except ExpiredSignatureError:
            return Response({"error": "El token ha expirado"}, status=status.HTTP_401_UNAUTHORIZED)
        except InvalidTokenError:
            return Response({"error": "El token es inválido"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
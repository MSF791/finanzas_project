from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioView, 'usuario')
router.register(r'ingreso', IngresoView, 'ingreso')
router.register(r'gasto', GastoView, 'gasto')
router.register(r'objetivo', ObjetivoAhorroView, 'objetivo')
router.register(r'presupuesto', PresupuestoView, 'presupuesto')
router.register(r'factura', FacturaView, 'factura')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', ObtainJwtToken.as_view(), name='obtain_jwt_token'),
    path('api/v1/token/load/', LoadJwtToken.as_view(), name='load_jwt_token'),
    path('api/v1/recordatorio/', NotificationBill.as_view(), name="notification_bill")
]
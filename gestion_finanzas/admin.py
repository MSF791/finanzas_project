from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(ObjetivoAhorro)
admin.site.register(Presupuesto)
admin.site.register(Factura)
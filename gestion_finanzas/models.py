from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    # Cambiar el related_name para evitar conflictos con el modelo User predeterminado
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Nombre personalizado para evitar conflictos
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set_permissions',  # Nombre personalizado para evitar conflictos
        blank=True,
    )
    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class Ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ingresos')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fuente = models.CharField(max_length=100)  # Ejemplo: Salario, Freelance, etc.
    fecha = models.DateField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.fuente} - {self.cantidad}"

class Gasto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='gastos')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)  # Ejemplo: Alquiler, Comida, etc.
    fecha = models.DateField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.categoria} - {self.cantidad}"

class ObjetivoAhorro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='objetivos_ahorro')
    nombre = models.CharField(max_length=100)  # Ejemplo: Vacaciones, Fondo de emergencia
    cantidad_objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_limite = models.DateField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - Objetivo: {self.cantidad_objetivo}"

class Presupuesto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='presupuestos')
    categoria = models.CharField(max_length=100)  # Ejemplo: Comida, Entretenimiento, etc.
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.categoria} - Presupuesto: {self.cantidad}"
    
class Factura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='facturas')
    nombre = models.CharField(max_length=100)  # Ejemplo: Factura de luz, Internet
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()
    pagada = models.BooleanField(default=False)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} - {self.fecha_vencimiento}"

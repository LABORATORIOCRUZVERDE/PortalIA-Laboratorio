from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):

    TIPO_DOCUMENTO = [
        ("CC", "Cédula de ciudadanía"),
        ("TI", "Tarjeta de identidad"),
        ("CE", "Cédula de extranjería"),
        ("PP", "Pasaporte"),
    ]

    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO)
    documento = models.CharField(max_length=20, unique=True)

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    fecha_nacimiento = models.DateField()

    sexo = models.CharField(max_length=1, choices=SEXO)

    celular = models.CharField(max_length=20)

    correo = models.EmailField(blank=True)

    direccion = models.CharField(max_length=200, blank=True)

    municipio = models.CharField(max_length=80, blank=True)

    acepta_habeas_data = models.BooleanField(default=False)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    activo = models.BooleanField(default=True)

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.documento} - {self.nombres} {self.apellidos}"
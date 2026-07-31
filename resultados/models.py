from django.db import models
from pacientes.models import Paciente


class Resultado(models.Model):

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name="resultados"
    )

    tipo_examen = models.CharField(max_length=100)

    fecha_resultado = models.DateField()

    archivo_pdf = models.FileField(upload_to="resultados/")

    nombre_archivo = models.CharField(
    max_length=100,
    blank=True,
    default=""
)

    fecha_carga = models.DateTimeField(auto_now_add=True)

    disponible = models.BooleanField(default=True)

    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.paciente} - {self.tipo_examen}"
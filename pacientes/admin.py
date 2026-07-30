from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):

    list_display = (
        "documento",
        "nombres",
        "apellidos",
        "celular",
        "correo",
        "activo",
    )

    search_fields = (
        "documento",
        "nombres",
        "apellidos",
    )

    list_filter = (
        "activo",
        "sexo",
    )
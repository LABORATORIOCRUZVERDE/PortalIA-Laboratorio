from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = [
            "tipo_documento",
            "documento",
            "nombres",
            "apellidos",
            "fecha_nacimiento",
            "sexo",
            "celular",
            "correo",
            "direccion",
            "municipio",
            "acepta_habeas_data",
        ]
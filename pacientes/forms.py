from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):

    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput()
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput()
    )

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

    def clean(self):

        cleaned_data = super().clean()

        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("password2")

        if p1 != p2:
            raise forms.ValidationError(
                "Las contraseñas no coinciden."
            )

        return cleaned_data
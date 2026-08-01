from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PacienteForm


def registro_paciente(request):

    if request.method == "POST":

        formulario = PacienteForm(request.POST)

        if formulario.is_valid():

    paciente = formulario.save(commit=False)

    documento = paciente.documento

    if User.objects.filter(username=documento).exists():

        messages.error(
            request,
            "Ya existe un usuario registrado con este documento."
        )

    else:

        usuario = User.objects.create_user(
            username=documento,
            password=formulario.cleaned_data["password"],
            first_name=paciente.nombres,
            last_name=paciente.apellidos,
            email=paciente.correo,
        )

        paciente.usuario = usuario

        paciente.save()

        messages.success(
            request,
            "Registro exitoso. Ya puedes iniciar sesión."
        )

        return redirect("login")

    else:

        formulario = PacienteForm()

    return render(
        request,
        "pacientes/registro.html",
        {"formulario": formulario},
    )
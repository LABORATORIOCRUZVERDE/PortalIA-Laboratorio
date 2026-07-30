from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import PacienteForm


def registro_paciente(request):

    if request.method == "POST":

        formulario = PacienteForm(request.POST)

        if formulario.is_valid():

            paciente = formulario.save(commit=False)

            usuario = User.objects.create_user(
                username=paciente.documento,
                password=paciente.documento
            )

            paciente.usuario = usuario

            paciente.save()

            return redirect("registro_paciente")

    else:

        formulario = PacienteForm()

    return render(
        request,
        "pacientes/registro.html",
        {"formulario": formulario},
    )
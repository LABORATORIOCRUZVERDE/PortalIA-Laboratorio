from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Resultado
from pacientes.models import Paciente


@login_required
def lista_resultados(request):

    paciente = Paciente.objects.get(usuario=request.user)

    resultados = Resultado.objects.filter(
        paciente=paciente
    ).order_by("-fecha_resultado")

    total_resultados = resultados.count()

    ultimo_resultado = resultados.first()

    return render(
        request,
        "resultados/lista_resultados.html",
        {
            "paciente": paciente,
            "resultados": resultados,
            "total_resultados": total_resultados,
            "ultimo_resultado": ultimo_resultado,
        },
    )
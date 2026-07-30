from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def login_usuario(request):

    if request.method == "POST":

        usuario = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=usuario,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("lista_resultados")

        else:

            return render(
                request,
                "usuarios/login.html",
                {
                    "error": "Usuario o contraseña incorrectos"
                }
            )

    return render(request, "usuarios/login.html")
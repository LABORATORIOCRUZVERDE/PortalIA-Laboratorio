import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from pacientes.models import Paciente
from resultados.models import Resultado
from django.core.files import File
from datetime import datetime
from lector_pdf import leer_pdf, extraer_datos

CARPETA_PDF = r"C:\PortalIA\Resultados"

archivos = os.listdir(CARPETA_PDF)

print("\nIMPORTANDO RESULTADOS\n")

for archivo in archivos:

    if not archivo.lower().endswith(".pdf"):
        continue

    # Verificar si ya fue importado
    if Resultado.objects.filter(nombre_archivo=archivo).exists():
        print(f"{archivo} ya fue importado.")
        continue

    ruta = os.path.join(CARPETA_PDF, archivo)

    texto = leer_pdf(ruta)

    datos = extraer_datos(texto)

    documento = datos.get("documento")

    try:

        paciente = Paciente.objects.get(documento=documento)

        print(f"Paciente encontrado: {paciente.nombres} {paciente.apellidos}")

    except Paciente.DoesNotExist:

        print(f"No existe un paciente con documento {documento}")

        continue

    print("------------------------------------")

    print("Archivo:", archivo)

    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

    print("------------------------------------")
    # Crear el registro del resultado

with open(ruta, "rb") as pdf:

    resultado = Resultado.objects.create(

        paciente=paciente,

        tipo_examen=datos["tipo_examen"],

        fecha_resultado=datetime.strptime(
            datos["fecha"],
            "%d/%m/%Y"
        ).date(),

        nombre_archivo=archivo,

        archivo_pdf=File(pdf, name=archivo)

    )

print("Resultado registrado correctamente.")
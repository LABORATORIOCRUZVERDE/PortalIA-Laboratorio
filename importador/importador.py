import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from pacientes.models import Paciente
from resultados.models import Resultado

from lector_pdf import leer_pdf, extraer_datos

CARPETA_PDF = r"C:\PortalIA\Resultados"

archivos = os.listdir(CARPETA_PDF)

print("\nIMPORTANDO RESULTADOS\n")

for archivo in archivos:

    if archivo.lower().endswith(".pdf"):

        ruta = os.path.join(CARPETA_PDF, archivo)

        texto = leer_pdf(ruta)

        datos = extraer_datos(texto)

        documento = datos.get("documento")

        try:

            paciente = Paciente.objects.get(documento=documento)

            print(f"Paciente encontrado: {paciente.nombres} {paciente.apellidos}")
            if Resultado.objects.filter(
    paciente=paciente,
    fecha_resultado=datos["fecha"]
).exists():

    print("Este resultado ya fue importado.")

    continue

        except Paciente.DoesNotExist:

            print(f"No existe un paciente con documento {documento}")

            continue

        print("------------------------------------")

        print("Archivo:", archivo)

        for clave, valor in datos.items():

            print(f"{clave}: {valor}")

        print("------------------------------------")
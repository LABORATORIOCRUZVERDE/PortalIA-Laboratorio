import re
import pdfplumber


def leer_pdf(ruta_pdf):

    texto = ""

    with pdfplumber.open(ruta_pdf) as pdf:

        for pagina in pdf.pages:

            contenido = pagina.extract_text()

            if contenido:
                texto += contenido + "\n"

    return texto


def extraer_datos(texto):

    datos = {}

    patron_documento = r"Identificación:(\d+)"
    patron_recepcion = r"Recepción:\s*(\d+)"
    patron_paciente = r"Paciente:\s*(.*?)\s+Recepción:"
    patron_fecha = r"Fecha rcp:\s*([0-9/]+)"
    patron_examen = r"1\s+(.+?)\s+Negativo"

    documento = re.search(patron_documento, texto)
    recepcion = re.search(patron_recepcion, texto)
    paciente = re.search(patron_paciente, texto)
    fecha = re.search(patron_fecha, texto)
    examen = re.search(patron_examen, texto)

    if documento:
        datos["documento"] = documento.group(1)

    if recepcion:
        datos["recepcion"] = recepcion.group(1)

    if paciente:
        datos["paciente"] = paciente.group(1).strip()

    if fecha:
        datos["fecha"] = fecha.group(1)

    if examen:
        datos["tipo_examen"] = examen.group(1).strip()

    return datos


if __name__ == "__main__":

    ruta = r"C:\PortalIA\Resultados\Result33595.pdf"

    texto = leer_pdf(ruta)

    datos = extraer_datos(texto)

    print("\nDATOS ENCONTRADOS\n")

    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
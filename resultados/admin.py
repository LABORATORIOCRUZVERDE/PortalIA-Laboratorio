from django.contrib import admin
from django.utils.html import format_html
from .models import Resultado


@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):

    list_display = (
        "paciente",
        "tipo_examen",
        "fecha_resultado",
        "disponible",
        "ver_pdf",
    )

    search_fields = (
        "paciente__documento",
        "paciente__nombres",
        "paciente__apellidos",
        "tipo_examen",
    )

    list_filter = (
        "disponible",
        "fecha_resultado",
    )

    ordering = (
        "-fecha_resultado",
    )

    list_per_page = 20

    date_hierarchy = "fecha_resultado"

    def ver_pdf(self, obj):
        if obj.archivo_pdf:
            return format_html(
                '<a class="button" href="{}" target="_blank">📄 Ver PDF</a>',
                obj.archivo_pdf.url
            )
        return "-"

    ver_pdf.short_description = "PDF"
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portal.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("pacientes/", include("pacientes.urls")),
    path("resultados/", include("resultados.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
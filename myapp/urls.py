# myapp/urls.py
from django.urls import path
from .views import pagina_dinamica, seleccionar_contenidos, correos_enviados, reenviar_correos

urlpatterns = [
    path('pagina-dinamica/', pagina_dinamica, name='pagina_dinamica'),
    path('seleccionar-contenidos/', seleccionar_contenidos, name='seleccionar_contenidos'),
    path('correos-enviados/', correos_enviados, name='correos_enviados'),
    path('reenviar_correos/', reenviar_correos, name='reenviar_correos'),

]

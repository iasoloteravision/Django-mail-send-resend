from django.urls import path
from .views import envio_html, mensaje_exito

urlpatterns = [
    path('<int:destinatario_id>/<int:html_id>/', envio_html, name='envio_html'),
    path('mensaje_exito/<int:destinatario_id>/', mensaje_exito, name='mensaje_exito'),
]

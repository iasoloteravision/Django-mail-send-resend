# myapp/admin.py
from django.contrib import admin
from .models import Destinatario, Contenido

admin.site.register(Destinatario)
admin.site.register(Contenido)

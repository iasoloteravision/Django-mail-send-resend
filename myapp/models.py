# myapp/models.py
from django.db import models


class Destinatario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Contenido(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    mostrar_en_pagina_dinamica = models.BooleanField(default=False)
    destinatario = models.ForeignKey(Destinatario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    

class CorreoEnviado(models.Model):
    asunto = models.CharField(max_length=255)
    cuerpo = models.TextField()
    destinatario = models.EmailField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=255, default='Correo Enviado')

    def __str__(self):
        return f'{self.asunto} - {self.destinatario}'

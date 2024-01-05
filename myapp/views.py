# myapp/views.py
from django.shortcuts import render, redirect
from .models import Contenido, Destinatario, CorreoEnviado
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


def pagina_dinamica(request):
    contenidos = Contenido.objects.all()
    destinatarios = Destinatario.objects.all()

    if request.method == 'GET' and 'seleccionados' in request.GET and 'destinatario' in request.GET:
        seleccionados = request.GET.getlist('seleccionados')
        destinatario_id = request.GET.get('destinatario')

        contenido_seleccionado = Contenido.objects.filter(id__in=seleccionados)
        destinatario = Destinatario.objects.get(id=destinatario_id)

        # Aquí obtenemos el contenido de la plantilla
        cuerpo_del_correo = "\n\n".join(
            [f"{contenido.titulo}:\n{contenido.cuerpo}" for contenido in contenido_seleccionado])

        # Aquí configuramos y enviamos el correo
        asunto = f"Contenido Seleccionado: {contenido_seleccionado[0].titulo}"
        mensaje = f"Estimado {destinatario.nombre},\n\nAquí está el contenido seleccionado:\n{cuerpo_del_correo}"

        send_mail(
            asunto,
            mensaje,
            # Remitente del correo (debes configurar un correo válido aquí)
            'jjusturi@gmail.com',
            [destinatario.correo],  # Lista de destinatarios
            # Cambia a True si no quieres que se generen excepciones en caso de errores
            fail_silently=False,
        )

        # Guarda el correo enviado en la base de datos
        correo_enviado = CorreoEnviado(
            asunto=asunto,
            cuerpo=mensaje,
            destinatario=destinatario,
        )
        correo_enviado.save()
        mensaje_exito = f"Correo enviado exitosamente a {destinatario.nombre} ({destinatario.correo})"
        return render(request, 'myapp/pagina_dinamica.html', {'contenidos': contenidos, 'destinatarios': destinatarios, 'mensaje_exito': mensaje_exito})

    return render(request, 'myapp/pagina_dinamica.html', {'contenidos': contenidos, 'destinatarios': destinatarios})


def seleccionar_contenidos(request):
    if request.method == 'POST':
        seleccionados = request.POST.getlist('contenidos')
        Contenido.objects.update(mostrar_en_pagina_dinamica=False)
        Contenido.objects.filter(id__in=seleccionados).update(
            mostrar_en_pagina_dinamica=True)
        return redirect('pagina_dinamica')

    contenidos = Contenido.objects.all()
    return render(request, 'myapp/seleccionar_contenidos.html', {'contenidos': contenidos})


def correos_enviados(request):
    correos_enviados = CorreoEnviado.objects.all()
    return render(request, 'myapp/correos_enviados.html', {'correos_enviados': correos_enviados})


def reenviar_correos(request):
    correos_enviados = CorreoEnviado.objects.all()
    destinatarios = Destinatario.objects.all()
    mensaje_exito = None

    if request.method == 'POST' and 'correos_seleccionados' in request.POST and 'destinatario' in request.POST:
        correos_seleccionados = request.POST.getlist('correos_seleccionados')
        destinatario_id = request.POST.get('destinatario')

        # Obtén el destinatario seleccionado
        destinatario = Destinatario.objects.get(id=destinatario_id)

        for correo_id in correos_seleccionados:
            correo = CorreoEnviado.objects.get(id=correo_id)

            # Configura y reenvía el correo
            asunto = f"Reenviado: {correo.asunto}"
            mensaje = f"Estimado {destinatario.nombre},\n\n{correo.cuerpo}"

            send_mail(
                asunto,
                mensaje,
                # Remitente del correo (debes configurar un correo válido aquí)
                'jjusturi@gmail.com',
                [destinatario.correo],  # Lista de destinatarios
                # Cambia a True si no quieres que se generen excepciones en caso de errores
                fail_silently=False,
            )

        mensaje_exito = f"Correos reenviados exitosamente a {destinatario.nombre} ({destinatario.correo})"

        # Almacena el mensaje de éxito en la sesión
        request.session['mensaje_exito'] = mensaje_exito

        # Redirige a la misma vista después de realizar la acción POST
        return redirect('reenviar_correos')
    
    # Recupera el mensaje de éxito de la sesión, si existe
    mensaje_exito = request.session.pop('mensaje_exito', None)

    return render(request, 'myapp/reenviar_correos.html', {'correos_enviados': correos_enviados, 'destinatarios': destinatarios, 'mensaje_exito': mensaje_exito})

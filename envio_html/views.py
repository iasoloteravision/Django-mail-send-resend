from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseNotFound
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myapp.models import Destinatario


def envio_html(request, destinatario_id, html_id):
    destinatario = get_object_or_404(Destinatario, id=destinatario_id)

    # Aquí asumo que tienes una lista de nombres de tus páginas HTML
    nombres_html = ['pagina1.html', 'pagina2.html']

    if html_id < 1 or html_id > len(nombres_html):
        return HttpResponseNotFound('Página HTML no encontrada')

    nombre_html_seleccionada = nombres_html[html_id - 1]

    # Carga el contenido de la página HTML seleccionada
    try:
        html_path = f'envio_html/{nombre_html_seleccionada}'
        contenido_html = render_to_string(html_path, {'destinatario': destinatario})
        cuerpo_del_correo = strip_tags(contenido_html)  # Elimina etiquetas HTML para el cuerpo del correo
    except Exception as e:
        return HttpResponseNotFound(f'Error al cargar la página HTML: {e}')

    # Configura y envía el correo
    asunto = f"Contenido HTML Seleccionado: {nombre_html_seleccionada}"
    mensaje = f"Estimado {destinatario.nombre},\n\nAquí está el contenido seleccionado:\n{cuerpo_del_correo}"

    try:
        send_mail(
            asunto,
            mensaje,
            'jjusturi@gmail.com',  # Remitente del correo (configura un correo válido aquí)
            [destinatario.correo],  # Lista de destinatarios
            fail_silently=False,
            html_message=contenido_html,  # Agrega el contenido HTML al correo
        )
        # Mensaje de éxito
        messages.success(request, f"Correo HTML enviado exitosamente a {destinatario.nombre} ({destinatario.correo})")

        # Redirige a una nueva vista o página
        return redirect('mensaje_exito', destinatario_id=destinatario_id)

    except Exception as e:
        messages.error(request, f"Error al enviar el correo HTML: {e}")
        return redirect('pagina_dinamica')  # O redirige a la página de error
   
    
def mensaje_exito(request, destinatario_id):
    destinatario = get_object_or_404(Destinatario, id=destinatario_id)
    return render(request, 'envio_html/mensaje_exito.html', {'destinatario': destinatario})

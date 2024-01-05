# Django template send & resend
![Static Badge](https://img.shields.io/badge/MAIL_SENDER-blue)
![Static Badge](https://img.shields.io/badge/PYTHON-yellow)
![Static Badge](https://img.shields.io/badge/DJANGO-green)
![Static Badge](https://img.shields.io/badge/Teravision-blue)


## Descripción

Este proyecto proporciona una plataforma para enviar correos electrónicos dinámicamente seleccionando plantillas y destinatarios. Incluye funcionalidades como la creación de contenidos, selección de destinatarios, envío de correos y reenvío de correos previamente enviados.

## Requisitos

- Python (versión 3.X)
- Django (versión 4.X)

## Configuración del Entorno**

1. Clona el repositorio:

```bash
git clone https://github.com/iasoloteravision/Django-mail-send-resend.git
cd pag_din
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Configura la base de datos:

```bash
python manage.py migrate
```

4. Crea un superusuario para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

5. Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

6. Accede al panel de administración en `http://localhost:8000/admin/` e inicia sesión con el superusuario creado.

7. Añade contenidos y destinatarios a través del panel de administración.

## Uso

1. Accede a la aplicación en `http://localhost:8000/`.
2. Selecciona los contenidos y destinatarios deseados.
3. Envía correos y visualiza el mensaje de éxito en `http://localhot:8000/pagina_dinamica/`
4. Explora la funcionalidad de reenviar correos previamente enviados en `http://localhot:8000/reenviar_correos/`

## Estructura del Proyecto

```bash
myapp/
|-- myapp/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   `-- ...
|-- templates/
|   `-- myapp/
|       |-- pagina_dinamica.html
|       `-- reenviar_correos.html
|-- manage.py
|-- requirements.txt
`-- README.md
```

## Contribuir

Si deseas contribuir al proyecto, sigue estos pasos:

1. Fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añade nueva característica'`).
4. Sube los cambios a tu fork (`git push origin feature/nueva-caracteristica`).
5. Abre un pull request.

## Licencia

Este proyecto está bajo la licencia [Nombre de la Licencia]. Consulta el archivo [LICENSE.md](LICENSE.md) para más detalles.

## Contacto

- [Imanol Asolo] - [iasolo@teravisiontech..com]
- Proyecto: [https://github.com/iasoloteravision/Django-mail-send-resend.git]

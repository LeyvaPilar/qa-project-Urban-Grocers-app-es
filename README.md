# Proyecto Urban Grocers 

Pilar Leyva Maldonado 
14vo grupo sprint 7


Este proyecto permite crear un usuario y un kit mediante solicitudes HTTP a un servicio web utilizando la librería `requests` en Python.
El flujo incluye la obtención de un token de autenticación tras crear un usuario, que se utiliza para autenticar las siguientes solicitudes.
 
## Los requisitos

Para ejecutar este proyecto, necesitas instalar las siguientes dependencias:

- Python 3.x
- Librería `requests`

## Instalación

Puedes instalar la librería `requests` ejecutando:

```bash
pip3 install requests
```

## Estructura

El proyecto contiene los siguientes archivos:

configuration.py
create_kit_name_kit_test.py
data.py
sender_stand_request.py

Es importante configurar correctamente `configuration.py` y `data.py` antes de ejecutar el código

### configuration.py

Estructura del código

```python
URL_SERVICE = "https://api.example.com"  # URL base del servicio
CREATE_USER_PATH = "/users/create"       # Ruta para crear un usuario
KITS_PATH = "/kits/create"               # Ruta para crear un kit
```

### data.py

Estructura del código

```python
user_body = {
    "name": "Nombre de usuario",
    "email": "usuario@example.com",
    "password": "password123"
}

kit_body = {
    "name": "a",
    "description": "Descripción del kit"
}

headers = {
    "Content-Type": "application/json"
}
```

### Uso
Sigue los siguientes pasos para ejecutar el código:

- Crea un usuario y obtén un token de autenticación:
- La función create_user_for_get_credentials() enviará una solicitud para crear un nuevo usuario.
- Si la creación es exitosa, obtendrá el token de autenticación (authToken) y lo añadirá a los encabezados.

### Crea un kit:
- La función one_number_allow_character() creará un kit utilizando el token de autenticación obtenido en el paso anterior. 
- La respuesta se verificará para asegurarse de que el kit tiene el nombre "a".

Para ejecutar el código, asegúrate de que todos los archivos están correctamente configurados y luego ejecuta el archivo principal:

```bash
pytest create_kit_name_kit_test.py
```
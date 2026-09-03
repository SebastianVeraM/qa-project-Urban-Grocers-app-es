import configuration
import requests
import data

# Crear sesión global para reutilizar la conexión
session = requests.Session()


def post_new_user(user_body):
    """Envía una solicitud POST para crear un nuevo usuario"""
    return session.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body,
        headers=data.headers
    )


def post_new_client_kit(kit_body, auth_token):
    """Envía una solicitud POST para crear un nuevo kit de producto"""
    headers = data.headers.copy()  # importante usar copy() para no modificar el original
    headers["Authorization"] = f"Bearer {auth_token}"
    return session.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )

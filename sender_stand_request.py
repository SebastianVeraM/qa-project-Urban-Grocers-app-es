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
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return session.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )


'''def get_user_info(auth_token):
    """Envía una solicitud GET para obtener información del usuario"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    return session.get(
        configuration.URL_SERVICE + configuration.GET_USER_PATH,
        headers=headers
    )


def update_kit(kit_id, updated_body, auth_token):
    """Envía una solicitud PUT para actualizar un kit existente"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    return session.put(
        configuration.URL_SERVICE +
        configuration.UPDATE_KIT_PATH.format(kit_id),
        json=updated_body,
        headers=headers
    )


def delete_kit(kit_id, auth_token):
    """Envía una solicitud DELETE para eliminar un kit"""
    headers = {"Authorization": f"Bearer {auth_token}"}
    return session.delete(
        configuration.URL_SERVICE +
        configuration.DELETE_KIT_PATH.format(kit_id),
        headers=headers
    )
'''

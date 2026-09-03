import sender_stand_request
import data

# --- Funciones auxiliares ---


def get_kit_body(name):
    """Devuelve una copia del cuerpo de solicitud con el nombre modificado"""
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


def get_new_user_token():
    """Crea un nuevo usuario y devuelve su token"""
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]


def positive_assert(kit_body):
    """Prueba positiva: espera código 201"""
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201


def negative_assert_code_400(kit_body):
    """Prueba negativa: espera código 400"""
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

# --- Pruebas ---


def test_create_kit_1_char_in_name():
    positive_assert(get_kit_body("a"))


def test_create_kit_511_chars_in_name():
    positive_assert(get_kit_body("a" * 511))


def test_create_kit_0_chars_in_name():
    negative_assert_code_400(get_kit_body(""))


def test_create_kit_512_chars_in_name():
    negative_assert_code_400(get_kit_body("a" * 512))


def test_create_kit_special_chars_in_name():
    positive_assert(get_kit_body("№%@"))


def test_create_kit_spaces_in_name():
    positive_assert(get_kit_body(" A Aaa "))


def test_create_kit_numbers_in_name():
    positive_assert(get_kit_body("123"))


def test_create_kit_no_name_param():
    negative_assert_code_400({})  # sin parámetro name


def test_create_kit_number_type_in_name():
    negative_assert_code_400(get_kit_body(123))


'''
# --- Pruebas GET ---


def test_get_user_info():
    token = get_new_user_token()
    response = sender_stand_request.get_user_info(token)
    assert response.status_code == 200
    assert "user" in response.json()

# --- Pruebas PUT ---


def test_update_kit_name():
    token = get_new_user_token()
    kit_body = get_kit_body("Kit inicial")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    kit_id = kit_response.json()["id"]

    updated_body = {"name": "Kit actualizado"}
    response = sender_stand_request.update_kit(kit_id, updated_body, token)
    assert response.status_code == 200
    assert response.json()["name"] == "Kit actualizado"

# --- Pruebas DELETE ---


def test_delete_kit():
    token = get_new_user_token()
    kit_body = get_kit_body("Kit para borrar")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    kit_id = kit_response.json()["id"]

    response = sender_stand_request.delete_kit(kit_id, token)
    assert response.status_code in [200, 204]
'''

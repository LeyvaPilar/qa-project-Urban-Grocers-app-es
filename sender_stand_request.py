import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=body,
                        headers=data.headers)

def positive_assert(kit_body):
    response_kit_body = post_new_kit(kit_body)
    assert response_kit_body.status_code == 201
    assert response_kit_body.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response_kit_body = post_new_kit(kit_body)
    assert response_kit_body.status_code == 400

# Login para obtener el token
def test_create_user_for_get_credentials():
    user_body = post_new_user(data.user_body)
    # Comprueba si el código de estado es 201
    assert user_body.status_code == 201
    # Actualizar el data.headers para usarse en las siguientes peticiones
    token = user_body.json()["authToken"]
    data.headers['Authorization'] = "Bearer " + token
# El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_one_number_allow_character():
    positive_assert(data.kit_body)
# El número permitido de caracteres (511):
# kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_the_number_character_allowed():
    positive_assert(data.kit_body_2)
# El número de caracteres es menor que la cantidad permitida (0):
# kit_body = { "name": "" }
def test_the_number_of_character_is_minor_than_quantity_allowed():
    negative_assert_code_400(data.kit_body_3)
# El número de caracteres es mayor que la cantidad permitida (512):
# kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_the_number_of_characters_is_bigger_than_maximum_quantity_allowed():
    negative_assert_code_400(data.kit_body_4)
# Se permiten caracteres especiales:
# kit_body = { "name": ""№%@"," }
def test_it_is_allowed_special_characters():
    positive_assert(data.kit_body_5)
# Se permiten espacios:
# kit_body = { "name": " A Aaa " }
def test_it_is_spaces_allowed():
    positive_assert(data.kit_body_6)
# Se permiten números:
# kit_body = { "name": "123" }
def test_it_is_allorwd_numbers():
    positive_assert(data.kit_body_7)
# El parámetro no se pasa en la solicitud:
# kit_body = { }
def test_the_parameter_cannot_pass_to_request():
    negative_assert_code_400(data.kit_body_8)
# Se ha pasado un tipo de parámetro diferente (número):
# kit_body = { "name": 123 }
def test_the_name_is_number():
    negative_assert_code_400(data.kit_body_9)

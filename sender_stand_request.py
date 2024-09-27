import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_kit(body):
    headers = data.headers.copy()
    token = post_new_user(data.user_body).json()["authToken"]
    headers["Authorization"] = f"Bearer {token}"
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


import sender_stand_request
import data

# El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_one_number_allow_character():
    sender_stand_request.positive_assert(data.kit_body)
# El número permitido de caracteres (511):
# kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_the_number_character_allowed():
    sender_stand_request.positive_assert(data.kit_body_2)
# El número de caracteres es menor que la cantidad permitida (0):
# kit_body = { "name": "" }
def test_the_number_of_character_is_minor_than_quantity_allowed():
    sender_stand_request.negative_assert_code_400(data.kit_body_3)
# El número de caracteres es mayor que la cantidad permitida (512):
# kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_the_number_of_characters_is_bigger_than_maximum_quantity_allowed():
    sender_stand_request.negative_assert_code_400(data.kit_body_4)
# Se permiten caracteres especiales:
# kit_body = { "name": ""№%@"," }
def test_it_is_allowed_special_characters():
    sender_stand_request.positive_assert(data.kit_body_5)
# Se permiten espacios:
# kit_body = { "name": " A Aaa " }
def test_it_is_spaces_allowed():
    sender_stand_request.positive_assert(data.kit_body_6)
# Se permiten números:
# kit_body = { "name": "123" }
def test_it_is_allorwd_numbers():
    sender_stand_request.positive_assert(data.kit_body_7)
# El parámetro no se pasa en la solicitud:
# kit_body = { }
def test_the_parameter_cannot_pass_to_request():
    sender_stand_request.negative_assert_code_400(data.kit_body_8)
# Se ha pasado un tipo de parámetro diferente (número):
# kit_body = { "name": 123 }
def test_the_name_is_number():
    sender_stand_request.negative_assert_code_400(data.kit_body_9)

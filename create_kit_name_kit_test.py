import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == name


def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400


# Prueba 1: El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)


# Prueba 2: El número permitido de caracteres (511)
def test_create_kit_511_letter_in_name_get_success_response():
    string_511 = ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                  "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                  "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                  "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd"
                  "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                  "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                  "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                  "cdabcdabcdabcdabcdabcdabcdabcC")
    kit_body = get_kit_body(string_511)
    positive_assert(kit_body)


# Prueba 3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Prueba 4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_in_name_get_error_response():
    string_512 = "a" * 512
    kit_body = get_kit_body(string_512)
    negative_assert_code_400(kit_body)

# Prueba 5: Se permiten caracteres especiales
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert('"№%"')

# Prueba 6: Se permiten espacios
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7: Se permiten números (como string)
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")

# Prueba 8: El parámetro no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# Prueba 9: Se ha pasado un tipo de parámetro diferente (número entero)
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)

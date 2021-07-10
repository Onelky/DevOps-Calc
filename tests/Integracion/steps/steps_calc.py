import api
from behave import given, when, then, step
from fastapi.testclient import TestClient
import json


@given("que deseo sumar dos numeros")
def step(context):
    # sirve para subir un servidor falso para probar la api
    context.app = TestClient(api.app)


@when('yo ingrese el numero {num1} y {num2}')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/sumar?num1={num1}&num2={num2}')
    assert context.api_response.status_code == 200


@then('el result {resultado} debe ser la suma de ambos')
def step_impl(context, resultado):
    print(resultado)
    print(context.api_response.json().get('resultado'))
    assert str(resultado) == str(context.api_response.json().get('resultado'))

# @given(u'Launch GITHUB app with "{user}" and "{password}"')
# def step_impl(context, user, password):
#     print("This is the given step with {user} and {password}".format(user, password))

import api
from behave import given, when, then, step
from fastapi.testclient import TestClient
import json


# Suma
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


# RESTA

@given("que deseo restar dos numeros")
def step(context):
    # sirve para subir un servidor falso para probar la api
    context.app = TestClient(api.app)


@when('yo ingrese los numeros {num1} y {num2}')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(f'/restar?num1={num1}&num2={num2}')
    assert context.api_response.status_code == 200


@then('el resultado {resultado} debe ser la resta de ambos')
def step_impl(context, resultado):
    print(resultado)
    print(context.api_response.json().get('resultado'))
    assert str(resultado) == str(context.api_response.json().get('resultado'))


# MULTIPLICACION

@given("que deseo multiplicar dos numeros")
def step(context):
    # sirve para subir un servidor falso para probar la api
    context.app = TestClient(api.app)


@when('ingrese el numero {num1} y {num2}')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(
        f'/multiplicar?num1={num1}&num2={num2}')
    assert context.api_response.status_code == 200


@then('el resultado {resultado} debe ser la multiplicacion de ambos')
def step_impl(context, resultado):
    print(resultado)
    print(context.api_response.json().get('resultado'))
    assert str(resultado) == str(context.api_response.json().get('resultado'))


# DIVISION

@given("que deseo dividir dos numeros")
def step(context):
    # sirve para subir un servidor falso para probar la api
    context.app = TestClient(api.app)


@when('introduzca los numeros {num1} y {num2}')
def step_implementation(context, num1, num2):
    context.api_response = context.app.get(
        f'/dividir?num1={num1}&num2={num2}')
    assert context.api_response.status_code == 200


@then('el resultado {resultado} debe ser la division de ambos')
def step_impl(context, resultado):
    print(resultado)
    print(context.api_response.json().get('resultado'))
    assert str(resultado) == str(context.api_response.json().get('resultado'))

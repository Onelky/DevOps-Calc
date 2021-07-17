from typing import Optional
from fastapi import FastAPI
from calc import Calculadora

app = FastAPI()
calculadora = Calculadora()


@app.get("/")
def read_root():
    return {"Nombre": "Onelky Hernandez Febles", "Matricula": "1078043"}


@app.get("/sumar")
def read_sumar(num1: int = 0, num2: int = 0):
    return {
        'resultado': calculadora.sumar(num1, num2)
    }


@app.get("/restar")
def read_sumar(num1: int = 0, num2: int = 0):
    return {
        'resultado': calculadora.restar(num1, num2)
    }


@app.get("/multiplicar")
def read_multi(num1: int = 0, num2: int = 0):
    return {
        'resultado': calculadora.multiplicar(num1, num2)
    }


@app.get("/dividir")
def read_multi(num1: int = 0, num2: int = 0):
    return {
        'resultado': calculadora.division(num1, num2)
    }

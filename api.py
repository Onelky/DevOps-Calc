from typing import Optional
from fastapi import FastAPI
from calc import Calculadora

app = FastAPI()
calculadora = Calculadora()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sumar")
def read_sumar(num1: int = 0, num2: int = 0):
    return {
        'resultado': calculadora.sumar(num1, num2)
    }

# API Calculadora

## Funcionalities

- Suma de dos n umeros 
- Resta de dos numeros
- Multiplicacion de dos numeros
- Division de dos numeros

# Requirements 

- Docker
- Python3
  
## Librerias 

fastapi
uvicorn
behave
coverage

# Pruebas 

## Pruebas unitarias

Se utiliza el siguiente comando:
```
  coverage run unit-tests.py 

```

> - Nota: En caso de que se tenga un virtual enviroment se utiliza el flag **--omit [directorio]**.
>  
> - Para especificar el porcentaje minimo que deben cubrir las pruebas, se utiliza **--fail-under=[porcentaje_minimo]**  

```
coverage run --omit 'mypython/*' -m unittest unit-tests.py && coverage report -m --fail-under=95

```


## Pruebas de integracion con behave 
Se utiliza este compando: **behave [carpeta_de_steps]**
```
behave tests 
```


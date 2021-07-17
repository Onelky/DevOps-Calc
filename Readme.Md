# Links a los demas repositorios 
* **Primera asignacion (API):** https://github.com/Onelky/Devops-T1-BlazorTemplate
  
* **Segunda asignacion (Wordpress):** https://github.com/Onelky/DevOps-Wordpress
  
# API Calculadora

## Descripcion
Esta es una aplicacion desarrollada en python que le permite al usuario recibir respuestas a distintas operaciones matematicas basicas (suma, multiplicacion, resta y division).

## Funcionalities

- Suma de dos numeros 
- Resta de dos numeros
- Multiplicacion de dos numeros
- Division de dos numeros

# Requirements 

- Docker
- Python3
  
## Librerias 

- fastapi
- uvicorn
- behave
- coverage

## Compilacion 
```
cd Calculadora-Python

```

## Ejecutar 

```
uvicorn --host 0.0.0.0 --port 8000 api:app

```

# Pruebas 

## Pruebas unitarias

```
 python unit-tests.py

```

### Validacion del coverage
Se utiliza el siguiente comando para validad la cobertura del codigo:
```
  coverage run unit-tests.py 

```

- Nota: En caso de que se tenga un virtual enviroment se utiliza el flag **--omit [directorio]**.
  
- Para especificar el porcentaje minimo que deben cubrir las pruebas, se utiliza **--fail-under=[porcentaje_minimo]**  

```
coverage run --omit 'mypython/*' -m unittest unit-tests.py && coverage report -m --fail-under=95

```


## Pruebas de integracion con behave 
Se utiliza este comando: **behave [carpeta_de_steps]**
```
behave tests 
```


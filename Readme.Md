# API Calculadora

## Descripcion
Esta es una aplicacion desarrollada durante la asignatura "DevOps y DevSecOps". Es una calculadora en python que le permite al usuario recibir respuestas a distintas operaciones matematicas basicas (suma, multiplicacion, resta y division). 
La misma fue realizada con el fin de simular varias etapas del ciclo de vida de una aplicacion (development, staging, production y testing) utilizando distintas herramientas de automatizacion de pruebas y varios pipelines de Github Actions. De esta manera, cada vez que se intenta hacer un commit en la rama principal, se ejecutan pruebas y solo se puede entrar en la siguiente etapa una vez aprobados el build, deployment y test de la etapa previa.   
  
  
## Funcionalities

- Suma de dos numeros 
- Resta de dos numeros
- Multiplicacion de dos numeros
- Division de dos numeros

## Branch strategy
La estrategia a utilizar es GitHub Flow, cada vez que se desarrolla un feature Each developer creates a new branch, the feature branch, for their changes from trunk.
Feature branches can be deployed to a testing environment for verification or pushed directly to trunk and deployed to a non-production environment from there.
A short-lived release branch may be used off trunk to prepare for and execute a release.

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



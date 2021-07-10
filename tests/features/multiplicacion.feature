Feature: Multiplicacion de dos numeros

  Scenario Outline: multiplicacion
     Given que deseo multiplicar dos numeros
      When yo ingrese el numero <num1> y <num2>
      Then el resultado <resultado> debe ser la multiplicacion de ambos 
  
    Examples: Amphibians
    | num1 | num2  | resultado     |
    |   7  |    2  |     14        |
    |   7  |    0  |     0         | 
    |   2  |   -5  |    -10        | 
    |   1  |  100  |     100       | 
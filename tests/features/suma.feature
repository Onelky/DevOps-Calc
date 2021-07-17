Feature: Sumar dos numeros

  Scenario Outline: suma
      Given que deseo sumar dos numeros
      When yo ingrese el numero <num1> y <num2>
      Then el result <resultado> debe ser la suma de ambos
    
      Examples: Sumas
      | num1 | num2  | resultado      |
      |   1  |    2  |     3          |
      |   2  | 2000  |     2002       | 
      |   0  |    0  |     0          | 
      |   -10 |   0 |      False        | 
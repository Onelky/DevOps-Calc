Feature: Dividir dos numeros

  Scenario Outline: dividion
     Given que deseo dividir dos numeros
      When yo ingrese el numero <num1> y <num2>
      Then el resultado <resultado> debe ser la division de ambos 
  
      Examples: Amphibians
      | num1 | num2  | resultado          |
      |   2  |    1  |     2              |
      |   0  |    0  |     "Invalido"     | 
      |   1  |    0  |     "Invalido"     | 
      |   0  |  100  |      0             | 
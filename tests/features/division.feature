Feature: Dividir dos numeros

  Scenario Outline: dividion
     Given que deseo dividir dos numeros
      When introduzca los numeros <num1> y <num2>
      Then el resultado <resultado> debe ser la division de ambos 
  
      Examples: Division
      | num1 | num2  | resultado |
      |   2  |    1  |     2     |
      |   0  |   -2  |     False | 
      |   1  |    0  |     False | 
      |   100  |  10  |    10    | 
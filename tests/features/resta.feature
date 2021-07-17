Feature: Restar dos numeros

  Scenario Outline: restar
     Given que deseo restar dos numeros
      When yo ingrese los numeros <num1> y <num2>
      Then el resultado <resultado> debe ser la resta de ambos 
  
      Examples: Restas
      | num1 | num2  | resultado    |
      |   2  |    2  |     0        |
      |4000  | 2000  |     2000     | 
      |   0  |    0  |     0        | 
      |  -3  |   -4  |     False     | 

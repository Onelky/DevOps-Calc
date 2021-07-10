Feature: Restar dos numeros

  Scenario Outline: restar
     Given que deseo restar dos numeros
      When yo ingrese el numero <num1> y <num2>
      Then el resultado <resultado> debe ser la resta de ambos 
  
      Examples: Amphibians
      | num1 | num2  | resultado                       |
      |   2  |    2  |     0                           |
      |4000  | 2000  |     2000                        | 
      |   0  |    0  |     0                           | 
      |   -3 |   -4  | "No se permiten negativos!"     | 
      |   4  |   -7  | "No se permiten negativos!"     | 
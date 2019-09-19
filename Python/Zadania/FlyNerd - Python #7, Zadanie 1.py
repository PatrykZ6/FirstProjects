# -*- coding: utf8 -*-

"""
Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

"""

for i in range(11):
  x = int((i*(1+i))/2)
  print (x)

"""
  0 + 1 = 1 
  1 + 2 = 3
  3 + 3 = 6
  6 + 4 = 10

-----------------------------

#inne rozwiązanie
for x in range(1,11):
    print(sum(lista[:x]))

"""

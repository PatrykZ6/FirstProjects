# -*- coding: utf-8 -*-

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

liczba = int(input("Podaj liczbę: "))

#[output] for [item] in [list] if [filter]
print([x for x in a if x < liczba])

#normalna pętla for
c=[]
for x in a:
  if x < liczba:
    c.append(x)  
print (c)

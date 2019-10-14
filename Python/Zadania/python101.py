# -*- coding: utf8 -*-


import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
print ("Wytypuj {} z {} liczb".format(ileliczb,maksliczba))

liczby = []
i=0
while i < ileliczb:
  los = random.randint(1, maksliczba)
  print (los)
  print (liczby.count(los) == 0)
  if liczby.count(los) == 0:
    liczby.append(los)
    i+=1
    
print (liczby)

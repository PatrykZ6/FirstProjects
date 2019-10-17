# -*- coding: utf8 -*-


import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
print ("Wytypuj {} z {} liczb".format(ileliczb,maksliczba))

"""
liczby = []
i=0
while i < ileliczb:
  los = random.randint(1, maksliczba)
  if ileliczb>maksliczba:
    print ("Nie możesz podać maksymalnej liczby mniejszej niż ilość typowanych liczb.")
    break
  elif liczby.count(los) == 0:
    liczby.append(los)
    i+=1

if liczby != []:
  print (liczby)  
"""
##################################################

liczby = set()
i=0
while i < ileliczb:
  if ileliczb>maksliczba:
    print ("Nie możesz podać maksymalnej liczby mniejszej niż ilość typowanych liczb.")
    break  
  los = random.randint(1, maksliczba)
  liczby.add(los)
  i=len(liczby)

if liczby != set():
  print (liczby)

strzaly = []
x=0
while x < ileliczb:
  strzal = int(input("Podaj {} liczbę: ".format(x+1)))
  if strzal < 0 or strzal > maksliczba:
    print ("Podałeś złą wartość, minimalna wartość to 1 a maksymalna to {}.".format(maksliczba))
  elif strzaly.count(strzal) != 0:
    print ("Podałeś jeszcze raz tą samą cyfrę.")
  else:
    strzaly.append(strzal)
    x+=1

trafione = liczby & set(strzaly)
print(strzaly)
print(trafione)
print ("Trafiłemś cyfr: {}. Te cyfry to: {}".format(len(trafione),trafione))

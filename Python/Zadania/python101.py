# -*- coding: utf8 -*-


import random
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
ileliczb = 0
while ileliczb<=0:
  ileliczb = int(input("Podaj ilość typowanych liczb: "))
  if ileliczb<=0:
    print ("Ilość typowanych liczb nie może być równa zeru ani nie może być liczbą ujemną")

maksliczba = 0
while ileliczb>maksliczba:
  maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
  if ileliczb>maksliczba:
    print ("Nie możesz podać maksymalnej liczby mniejszej niż ilość typowanych liczb.")

liczby = set()
i=0
while i < ileliczb:
  los = random.randint(1, maksliczba)
  liczby.add(los)
  i=len(liczby)

print ("Wytypuj {} z {} liczb".format(ileliczb,maksliczba))
#print (liczby)

for z in range(3):
  strzaly = []
  x=0
  while x < ileliczb:
    strzal = int(input("Podaj {} liczbę: ".format(x+1)))
    if strzal < 0 or strzal > maksliczba:
      print ("Podałeś złą wartość, minimalna wartość to 1 a maksymalna to {}.".format(maksliczba))
    elif strzaly.count(strzal) != 0:
      print ("Podałeś jeszcze raz tą samą liczbę.")
    else:
      strzaly.append(strzal)
      x+=1
  trafione = liczby & set(strzaly)
  #print(strzaly)
  #print(trafione)
  print ("Trafione liczby: {}. Te liczby to: {}".format(len(trafione),(", ".join(str(x) for x in trafione))))
  if (set(strzaly) != set(trafione) and z != 2):
    print("\n####################################################\n\nSpróbuj jeszcze raz!")
  elif set(strzaly) == set(trafione):
    print("Brawo! Zgadłeś wszystkie liczby :)")
    break
  else:
    break

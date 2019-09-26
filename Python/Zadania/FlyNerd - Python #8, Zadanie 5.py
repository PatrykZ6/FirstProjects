# -*- coding: utf8 -*-

"""
Korzystając z modułu random stwórz kolejną prostą grę. Komputer losuje słowo z dostępnego zakresu (posiada listę słów). Następnie litery są mieszane.
Wymieszane litery pokazywane są graczowi. Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku. Dopiero zgadnięcie przerywa grę.

Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”, aby zakończyć grę przed czasem.

"""

import random

print("Ułóż słowo z rozsypanych liter. Jeśli chcesz zakończyć grę wcześniej wpisz Q")

pula = ["rower", "młotek", "samuraj", "bumerang", "kajak"]

los = (random.choice(pula))

#print(los)

podzielone_litery = [los[i:i+1] for i in range(0, len(los), 1)]  #dzieli litery w słowie na pojedyńcze wartości listy

#print(podzielone_litery)
slowo = []
while (podzielone_litery != []):
  jedna_litera = random.choice(podzielone_litery)
  podzielone_litery.remove(jedna_litera) 
  #print(jedna_litera)
  #print(podzielone_litery)
  slowo.append(jedna_litera) 
  slowo=[' '.join(slowo)]
print (slowo[0].upper())

strzal = ''
while (strzal != los):
  strzal = input("Podaj słowo:\n").lower()
  if (strzal == 'q'):
    break
  elif (strzal == los):
    print ("Brawo! Udalo ci się zgadnąć!")
  else:
    print ("Niestety to nie jest to słowo. Spróbuj jeszcze raz.")

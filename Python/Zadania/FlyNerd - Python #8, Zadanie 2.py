# -*- coding: utf8 -*-
"""
Zapoznaj się z modułem random.

>>> import random
Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie.

"""

import random
randomowa_cyfra = random.randint(1, 21)
print(randomowa_cyfra)

print("Zgadnij cyfrę jaką wylosował komputer od 1-20\n")
strzal = 0
proba = 1
while (randomowa_cyfra != strzal):
  strzal = int(input("Podaj cyfrę: "))
  if (randomowa_cyfra != strzal):
    print("Nie trafiłeś, spróbuj jeszcze raz.")
  proba += 1
print("Brawo! Zgadłeś za {} razem! Liczba którą wylosował komputer to".format(proba), randomowa_cyfra)

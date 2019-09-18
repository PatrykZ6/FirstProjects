# -*- coding: utf8 -*-

"""
Trzy dowolne liczby zapisz do trzech zmiennych.
Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej.

"""

x = 12
y = 34
z = 5

lista = [x, y, z]
print (lista)

lista.sort()
print (lista)

print ("Największa wartośc w tabeli to:",lista[-1])
print ("Najmniejsza wartośc w tabeli to:",lista[0])

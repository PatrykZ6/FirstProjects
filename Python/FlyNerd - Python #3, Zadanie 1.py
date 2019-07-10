# -*- coding: utf8 -*-

"""
A.Utwórz nowy plik, który po podaniu przez użytkownika długości w cm będzie wyświetlał wynik w metrach i calach zaokrąglając do 4 miejsc po przecinku.
B.Podobny skrypt możesz wykonać dla zamiany kg na funty.
Wynik wyświetl używając dowolnego sposobu formatowania tekstu.
"""

cm = input("Podaj wartość w centymetrach: ")
m = int(cm)/100
cal = int(cm) / 2.54
print ("""
Po przeliczeniu {0} cm na metry i cale otrzymujemy wyniki:
{0} cm = {1:.4f} m
{0} cm = {2:.4f}"
""".format(cm, m, cal))


kg = input ("Podaj wartość w kilogramach: ")
funt = float(kg) * 2.20462262
print("""
Po przeliczeniu {0} kg na funty otrzymujemy wynik:
{0} kg = {1:.4f} lb
""".format(kg, funt))

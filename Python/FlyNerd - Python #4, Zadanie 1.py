# -*- coding: utf8 -*-

"""
Utwórz i wyświetl dowolne zmienne przechowujące wartości wg. typów:
Liczby (Numbers) - całkowite/zmiennoprzecinkowe
Teksty (String)
Typ logiczny (Bool)
Listy (List)
Krotki (Tuple)
Słowniki (Dictionary)
"""

liczba_int = int(4)
liczba_float = float(10.43)
tekst = str('elo ziomek')
logiczny = True
lista = [3.5,"mandarynki",False]
krotka = (3.5,"parówka",True)
slownik = {"lubie":"placki","jestem":"rudy","for":"honor"}

print("liczba int: ", liczba_int,"\n",type(liczba_int))
print("liczba float: ", liczba_float,"\n",type(liczba_float))
print("tekst: ", tekst,"\n",type(tekst))
print("logiczny: ", logiczny,"\n",type(logiczny))
print("lista: ", lista[1],"\n",type(lista))
# Listy przechowują różne element poprzedzielane przycinkiem umieszczone w nawiasie kwadartowym.
# Elementy na liście mogą mieć różne typy.
# Listy pozwalają na modyfikacje elementów, możemy podmienić element na liście.
# Listy są indeksowane (numerowane) od 0 – oznacza to, że żeby dostać się do pierwszego elementu musimy wpisać lista[0].
# Aby podmienić pierwszy element na liście wystarczy lista[0] = 4.

print("krotka: ", krotka ,"\n",type(krotka))
# Krotki to listy, które są niezmienne.
# Nie można zmodyfikować elementów zawartych w krotce.
# Krotka, tak jak stringi jest niemutowalna.
# Krotki umieszczamy w nawiasach okrągłych. 

print("słownik: ", slownik["jestem"],"\n",type(slownik))
# Słowniki są bardzo przydatnym typem danych.
# W innych językach programowania pojawiają się jako tablica haszująca, tablica asocjacyjna czy mapa.
# Przechowuje dane w parach jako klucz : wartość,
# z czego klucz musi być niemutowalnego typu oraz unikalny w obrębie słownika (klucz nie może się powtarzać!).
# Słownik jest strukturą nieuporządkowaną, w związku z czym nie można odwołać się do elementów słownika po indeksie.
# Jeśli istnieje klucz o wartości 0, otrzymamy wartość słownika jak w przykładzie powyżej niezależnie,
# którym z kolei elementem w słowniku jest para 0 : "zero".
# Warto wiedzieć, że jeśli spróbujemy przypisać wartości do nieistniejącego klucza,
# spowoduje to automatyczne powiększenie słownika – stworzenie takiego klucza i przypisanie mu wartości.
# Slownik.keys() – zwraca klucze w słowniku
# Slownik.values() – zwraca wartości w słowniku
# "herbata" in Slownik – zwróci prawdę jeśli klucz występuje w słowniku.

"""
wynik:
liczba int:  4 
 <class 'int'>
liczba float:  10.43 
 <class 'float'>
tekst:  elo ziomek 
 <class 'str'>
logiczny:  True 
 <class 'bool'>
lista:  mandarynki 
 <class 'list'>
krotka:  (3.5, 'parówka', True) 
 <class 'tuple'>
słownik:  rudy 
 <class 'dict'>
 """

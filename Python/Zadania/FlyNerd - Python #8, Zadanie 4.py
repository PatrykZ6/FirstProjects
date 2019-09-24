# -*- coding: utf8 -*-
"""
Napisz skrypt obliczający wartość silni. Rozwiąż zadanie za pomocą pętli for oraz pętli while.
Wejście: „Podaj dowolną liczbę całkowitą do 15:” 4
Wyjście: 4! = 24

"""


n = int(input("Prosze podac liczbe: "))
 
def silnia_rek(n):
#Obliczanie silni rekurencyjnie
  if (n>1):
    return n*silnia_rek(n-1)    #wywolanie rekurencyjne funkcji
  elif n in (0,1):
    return 1;
 
def silnia_iter(n):
#Obliczanie silni iteracyjnie
  silnia_tmp=1 #zmienna pomocnicza
  if n in (0,1):  #gdy n = 0 lub 1 zwroc 1
    return 1
  else:
    for i in range(2,n+1):  #gdy n>1 mnoz przez kolejne liczby od 2 do n
      silnia_tmp = silnia_tmp*i
    return silnia_tmp
 
print (silnia_rek(n))
print (silnia_iter(n))

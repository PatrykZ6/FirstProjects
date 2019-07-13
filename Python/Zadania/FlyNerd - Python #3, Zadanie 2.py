# -*- coding: utf8 -*-

"""
Napisz skrypt, który obliczy stan konta za kilka lat.
Program pyta użytkownika o:
- stan początkowy konta,
- stopę oprocentowania rocznego
- liczbę lat na lokacie
Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu.
Wypisz np. takie zdanie:
Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
"""

stan_konta = float(input ("Jaki jest stan początkowy konta: "))
stopa_oprocentowania = float(input("Jaka jest stopa oprocentowania konta: "))
liczba_miesiecy = int(input("Na ile miesięcy lokata: "))
zysk = float(stan_konta*stopa_oprocentowania/100*liczba_miesiecy/12)
wynik = zysk + stan_konta
print("""Twoje {} zł przez {} miesiące na lokacie {}% urośnie do {:.2f} zł
Twój zysk wynosi {:.2f} zł""".format(stan_konta,liczba_miesiecy,stopa_oprocentowania,wynik,zysk))

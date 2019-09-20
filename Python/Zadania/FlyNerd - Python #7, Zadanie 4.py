# -*- coding: utf8 -*-

"""
Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony

"""

ile = int(input("Ile razy ma się wykonać program?\n"))
for x in range(ile):
  wiel = int(input("Jaką liczbę mam sprawdzić? "))
  if (wiel%3 == 0 and wiel%4 == 0):
    print ("Hura!!!")
  if (wiel%3 != 0 and wiel%4 != 0):
    print ("*")
  if (wiel%3 == 0):
    print (wiel,"jest wielokrotnością liczby 3")
  else:
    print (wiel,"nie jest wielokrotnością liczby 3")
  if (wiel%4 == 0):
    print (wiel,"jest wielokrotnością liczby 4")
  else:
    print (wiel,"nie jest wielokrotnością liczby 4")

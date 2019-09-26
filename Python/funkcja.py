# -*- coding: utf8 -*-

"""
Dodaj funkcję nazwaną lista_korzysci() – która zwraca tablicę następujących napisów: "Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"

Dodaj funkcję nazwaną buduj_zdanie(info), która otrzymuje pojedynczy argument zawierający napis i zwraca zdanie zaczynające się podanym napisem i kończące się " jest zaleta funkcji!"

Wykonaj i zobacz jak funkcje ze sobą współpracują.

"""

tablica = ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]

def buduj_zdanie(info):
  if (type(info) == list):
    for x in range(len(info)):
      print (tablica[x],"jest zaleta funkcji!")
      x+=1
  else:
    print (info,"jest zaleta funkcji!")


buduj_zdanie(tablica) #tablica / tablica[0-3]
#gdy podamy wartość funkcji tablica, wyświetlą się na ekranie wysztkie elementy z dopiskeim "jest zaleta funkcji!"
#gdy podamy wartość funkcji tablica[index jednej z wartości listy], wyświetli się tylko wywołana wartość z listy z dopsikiem "jest zaleta funkcji!"

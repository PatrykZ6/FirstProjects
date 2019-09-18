# -*- coding: utf8 -*-

"""
1. Utwórz zbiór imion męskich i żeńskich. 
2. Poproś użytkownika o podanie imienia. 
3. Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację. Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.” 
4. Następnie użytkownik poda informację czy imię jest męskie czy żeńskie. 
5. Dodaj imię do listy.
"""
#1
M = "Mężczyzna"
K = "Kobieta"
lista_imion = {"Patryk":M, "Kasia":K, "Jarek":M, "Bartek":M, "Sebastian":M, "Milena":K}

print (list(lista_imion.keys()))

#2
imie = input("Podaj imię: ")
#lista_imion.append(imie)  #dodawanie imienia do listy
#print (lista_imion)

#3
wynik = imie in lista_imion.keys()   #sprawdza czy imie jest na liście kluczy słownika

if ( wynik == True ):
  print(imie,"to",lista_imion[imie].lower())  #łączone polecenie lista_imion[imie] pokazuje wartość dla klucza imie, a lower() zmienia wartość (string) na małe litery  
else:
  print("Nie znamy tego imienia.")
#if (wynik = false)

#4
if (imie not in lista_imion.keys()):
  plec = input("Podaj płeć (Mężczyzna = M / Kobieta = K): ")
  if (plec == "K"):
    plec = K
    print (plec)
  elif (plec == "M"):
    plec = M
    print (plec)
  else:
   print("Zła wartość")

#5
if (imie in lista_imion.keys()):
  print("Te imie jest już w bazie!")
  print("\n",lista_imion)
elif (plec == K or plec == M):
  lista_imion[imie] = plec 
  print("\n",lista_imion)

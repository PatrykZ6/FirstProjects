# -*- coding: utf8 -*-

"""
Pobierz od użytkownika imię, nazwisko i numer telefonu,
a następnie:
    * Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
    * Imię nazwisko popraw na pisane z dużej litery
    * Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
    * Sprawdź czy użytkownik jest kobietą
    * Połącz dane w jeden ciąg za pomocą spacji
    * Policz liczbę wszystkich znaków ww napisie
    * Podaj liczbę tylko liter w napisie
"""

name = input ("Podaj imię: ")
surname = input ("Podaj nazwisko: ")
tel = input ("Podaj swój numer telefonu: ")

print ("\nCzy imię składa się tylko z liter?", name.isalpha())
print ("Czy nazwisko składa się tylko z liter?", surname.isalpha())
print ("Czy numer telefonu składa się tylko z cyfr?", tel.isdigit())

print ("\nImię nazwisko popraw na pisane z dużej litery:")
name = name.capitalize()
surname = surname.capitalize()
print (name,surname)

print ("\nNiektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru:")
tel = tel.replace(" ", "")
tel = tel.replace("-","")
print (tel)

print ("\nCzy użytkownik jest kobietą?")
if name[-1] == 'a':
    print ("Tak, jest kobietą")
else:
    print ("Nie, nie jest kobietą")

print("\nCzy to imię kobiece?", name.endswith("a"))

print ("\nPołącz dane w jeden ciąg za pomocą spacji:")
personal = name+" "+surname+" "+tel
print (personal)

print ("\nPolicz liczbę wszystkich znaków ww napisie:")
print (len(personal))

print ("\nPodaj liczbę tylko liter w napisie:")
letters = len(personal) - personal.count(" ") - 9
print (letters)
personal = name+surname #sprawdzenie
print (len(personal))

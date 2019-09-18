# -*- coding: utf8 -*-

"""
Zapytaj użytkownika o wiek.
W zależności od wieku zwróć czy użytkownik jest już pełnoletni
lub ile lat zostało mu do pełnoletności,
Użytkownikom powyżej 100lat życz 200 ;)
"""

#print (1 == 1 and 2 < 1 or 1 != 2)

#print ("keb" not in "kebab")

"""
x = range(2, 5)
for n in x:
  print(n)
age = 15
#print ( 18-age == n[1])

print("Double the list numbers using for loop and range() function")
sampleList = [1, 2, 3, 4, 5]
for i in range(len(sampleList)):
    print( 2 <= sampleList[i] <= 4)
"""

print("Ile masz lat?")
age = int( input() )
if ( 18 <= age < 100 ):
    print("Jesteś dorosłym człowiekiem")
elif ( age >= 100 ):
    print("To naprawdę twój wiek?")
else:
    if ( 18-age == 1 ):
      print("Został Ci do pełnoletności jeszcze {} rok".format(18-age))
    elif ( 2 <= 18-age <=4  ):
      print("Zostały Ci do pełnoletności jeszcze {} lata".format(18-age)) 
    else:
      print("Zostało Ci do pełnoletności jeszcze {} lat".format(18-age))

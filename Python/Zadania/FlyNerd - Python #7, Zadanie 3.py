# -*- coding: utf8 -*-

"""
Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.

"""

#imiona = [x for x in input("Wprowadź parę imion oddzielając je spacjami: ").split()]
imiona = input("Wprowadź parę imion oddzielając je przecinakmi: ").split(",")
imiona = [x.strip(' ').capitalize() for x in imiona]  #funkcja która usuwa spacje i zmienia na pierwszą dużą literę
print(imiona)

for i in imiona: 
  print ('Cześć',i)

# -*- coding: utf8 -*-

"""
Do zmiennej zapisz zdanie: „Kurs Pythona jest prosty i przyjemny.”,
    * Policz znaki w napisie
    * Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
    * Wyświetl znak o indeksie:
        7
        12
        -4
        37
    * Wprowadź do zdania 2 błędy ortograficzne
"""

sentence = "Kurs Pythona jest prosty i przyjemny."

print (sentence,"\n")
print ("Policz znaki w napisie:\n",len(sentence),"\n")

print ("Nie modyfikując zmiennej sentence wyświetl słowo „prosty”:")
prosty = sentence.split(' ')
print (prosty[3],"\n")

print ("Wyświetl znak o indeksie: 7, 12, -4, 37:")
print("znak o indeksie 7: ", sentence[7])
print("znak o indeksie 12:", sentence[12])
print("znak o indeksie 4 od końca:", sentence[-4])
print("znak o indeksie 37 nie istnieje. Zdanie ma 37 znaków numerowane od 0 - 36,\
      ostatni znak to kropka:", sentence[36], "\n")

print ("Wprowadź do zdania 2 błędy ortograficzne")
sentence = sentence.replace('u','ó',1)
sentence = sentence.replace('rz','ż',1)
print (sentence)

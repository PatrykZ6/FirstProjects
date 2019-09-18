# -*- coding: utf8 -*-

"""
Trójkąt pitagorejski, to trójkąt prostokątny, którego boki są wyrażone liczbami naturalnymi a, b, c związanymi warunkiem: a2+b2=c2.

a) Poproś użytkownika o podanie długości boków A, B i C i sprawdź czy w ogóle możliwe jest utworzenie z nich trójkąta 🙂

b) Odpowiedz czy trójkąt jest trójkątem pitagorejskim.

c) Szczególnym przypadkiem jest trójkąt egipski o stosunkach długości 3:4:5. Sprawdź czy trójkąt pitagorejski jest trójkątem egipskim.

d) Uwzględnij, że kolejność danych nie musi mieć znaczenia! Tzn. długość C użytkownik może podać jako pierwszą wartość. Przypomnij sobie zadanie 3 🙂

Przykładowe dane:

nie-trójkąty: [6, 9, 20], [3, 6, 11], [31, 14, 17] - najdłuższy bok nie może przekraczać długości dwóch pozostałych boków
trójkąty nie-pitagorejskie: [4, 4, 4], [31, 17, 16], [10, 5, 8]
trójkąty pitagorejskie: [3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 40, 41], [8, 15, 17]
trójkąty egipskie: [9, 12, 15], [3, 4, 5], [15, 20, 25], [6, 8, 10]

"""

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))
c = int(input("Podaj długość boku c: "))

triangle = [a, b, c]
triangle.sort()
#print (triangle)

if (triangle[0]+triangle[1]<=triangle[2]):
  print ("To nie jest trójkąt.")
elif (triangle[0]**2+triangle[1]**2 == triangle[2]**2):
  if (triangle[0]%3 == 0 and triangle[1]%4 == 0 and triangle[2]%5 == 0):
    print ("Trójkąt egipski!!!")
  else:
    print ("Trójkąt pitagorejski!")
else:
  print ("To zwykły trujkąt.")

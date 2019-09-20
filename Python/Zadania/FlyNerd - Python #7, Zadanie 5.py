# -*- coding: utf8 -*-

"""
Spróbuj wyświetlić choinkę z trójkątów w taki sposób, aby każdy poziom choinki był o 1 wiersz dłuższy:

#
##
#
##
###
#
##
###
####

"""
choinka = 7
print ("\n",6*" "+2*"#")
print (6*" "+4*"#")
for i in range(3):
    for j in range(3, choinka):
      print(((8-j)*" "+j * "#")+(j*"#"))
    choinka+=1
for i in range(2):
  print (6*" "+4*"#")


#albo
print("\n")

j=int(input("podaj ile # ma mieć największa choinka? "))
m=3
for i in range(0, j):
    for k in range(1, m):
        print(k * "#")
    m+=1

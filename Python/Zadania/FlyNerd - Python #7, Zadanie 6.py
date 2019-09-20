# -*- coding: utf8 -*-

"""
Wyświetl w konsoli klasyczną tabliczkę mnożenia. W razie wątpliwości jak sformatować, by w konsoli pojawiła się tabela warto sobie przypomnieć odcinek 3 – formatowanie napisów w Pythonie.

"""

szer = 88
print("=" * szer)
print("|  x  ||   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |   10  |")
print("=" * szer)
zakres = 11
for x in range(1, zakres):
  print("| {:2}  ||  {:2}   |  {:2}   |  {:2}   |  {:2}   |  {:2}   |  {:2}   |  {:2}   |  {:2}   |  {:2}   |  {:3}  |" .format(x, x*1, x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9,x*10))
print("=" * szer)

# -*- coding: utf8 -*-

"""
Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i jego oceny.
Dodaj do swojego spisu.
"""


serial = {
    "Stranger Things" : 10,
    "Piraci" : 9,
    "Gra o tron" : 7,
    "Dark" : 8,
    "Czarnobyl" : 9
    }
print(list(serial.keys()))
#
"""
jaki_serial = input("Jaki serial chcesz obejrzeć?: ")
print("Serial '{}' ma ocenę {}/10".format(jaki_serial,serial[jaki_serial]))
"""
wprowadz_serial = input("Jaki serial wprowadzić do bazy?: ")
jaka_ocena = int(input("Jak go oceniasz od 1 do 10: "))
serial[wprowadz_serial] = jaka_ocena


print("{}".format(serial.keys()))
print(list(serial.values()))

# results = [1,2,3,4]
# p_results = [5,6,7,8]

# for result,p_result in zip(results,p_results):
#     print('{:3}{:20}'.format(result,p_result))


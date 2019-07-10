# -*- coding: utf8 -*-

"""
kalkulator zapotrzebowania kalorycznego 2
Zapisz kalkulator BMR, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""
#10 x masa ciała + 6.25 x wzrost w cm – 5 x wiek + S

masa = float(input( "Masa ciała w kg: " ))
wzrost = float(input( "Wzrost w cm: " ))
wiek = int(input( "Wiek: " ))
S = 5
kalorie = (10 * masa + 6.25 * wzrost - 5 * wiek + S)*1.6
print ("Powinieneś spożywać dziennie {} kalorii".format(kalorie))


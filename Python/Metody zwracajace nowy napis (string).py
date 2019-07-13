# -*- coding: utf8 -*-

text = "lubie Jeść KaBanosy"
star1 = 4
star2 = (32*2)-star1

print ("Oryginalny tekst: ",text,"\n")
print ("{:32s}".format("text.lower():"),text.lower())
print ("{:32s}".format("text.upper():"),text.upper())
print ("{:32s}".format("text.capitalize():"),text.capitalize())
print ("{:32s}".format("text.title():"),text.title())
print ("{:32s}".format("' '.join(text):")," ".join(text))
print (star1*"-","LUB:",star2*"-")
print ("{:32s}".format("'*'.join(text):"),"*".join(text))
print ("{:32s}".format("'   bez spacji'.lstrip(): "),"   bez spacji".lstrip())
print ("{:32s}".format("'bez spacji   '.rstrip(),':'",),"bez spacji   ".rstrip(),":")
print ("{:32s}".format("'  bez spacji  '.strip(),':'"),'  bez spacji  '.strip(),':')
print (star1*"-","LUB:",star2*"-")
print ("{:32s}".format("'bez spacjib'.strip('b'),':'"),'bez spacjib'.strip('b'),':')
print ("{:32s}".format("max('katakumby'): "), max('katakumby'))
print ("{:32s}".format("min('katakumby'): "), min('katakumby'))
print ("{:32s}".format("text.split(' ')"),text.split(' '))
print (star1*"-","LUB:",star2*"-")
print ("{:32s}".format("'02,04,1994'.split(',')"),'02,04,1994'.split(','))
print ("{}".format("'text w \\n dwóch liniach'.splitlines():"),'text w\ndwóch liniach'.splitlines()) 
print ("{:32s}".format("text.replace(' ','-'): "),text.replace(' ','-'))

"""
Opis metod na:
https://docs.google.com/spreadsheets/d/1ggHIjYyXiSYRwYGzfQnmV5_BNeevAeVgfMtMTZW4CZg/edit#gid=0
"""

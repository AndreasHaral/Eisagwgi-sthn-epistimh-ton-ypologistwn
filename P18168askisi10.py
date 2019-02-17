import urllib2
dief=raw_input("Dwse Url me http:")
req1=urllib2.Request(dief)
html=urllib2.urlopen(req1).read()
sind=0#Gia Sindesmous
sumbrp=0#Gia Br kai P
from HTMLParser import HTMLParser
class class1(HTMLParser):
    def metritis(self,tag,attrs):#pairnoyme aparaitita stoixeia apo ton kwdika html
        if tag=="link" or tag=="a":#gia sindesmous
            global sind
            sind=sind+1
        if tag=="p" or tag=="br":#gia allages grammhs apo br kai p
            global sumbrp
            sumbrp=sumbrp+1

help1=class1()
help1.feed(html)
print ('Gia Sindesmoys',sind)
print('Gia Br h P',sumbrp)
            



import urllib2
dief=raw_input("Δώσε διευθηνση σελιδας με http:")
req1=urllib2.Request(dief)
html=urllib2.urlopen(req1).read()
sind=0#Gia Sindesmous
sumbrp=0#Gia Br kai P
from HTMLParser import HTMLParser
class class1(HTMLParser):
    def metritis(self,tag,attrs):
        if tag=="link" or tag=="a":
            global sind
            sind=sind+1
        if tag=="p" or tag=="br":
            global sumbrp
            sumbrp=sumbrp+1

help1=class1()
help1.feed(html)
print (sind,sumbrp)
            



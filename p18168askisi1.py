size=input("posa diasthmata tha dwseis?")
w, h = size, 5;
lista = [[0 for x in range(w)] for y in range(h)] 
for i in range (size):
        lista[i][0]=input("dwse arxh")
        lista[i][1]=input("dwse telos")
#to parapanw kommati kodika xrisimopoieite gia na paroume tis eisodoys apo ton xristi     
def sumIntervals(lista):
    kenhlista = []
    size=len(lista)
    for i in range(size):
        for j in range(lista[i][0], lista[i][1]):#kanoyme px to [6,10] ginete[6,7,8,9,10]
            #epomenos to megethos tis neas listas einai to diasthma opou psaxnoume
            kenhlista.append(j)
    kenhlista= set(kenhlista)#methodos opou afairoume ta diastimata opou epikaliptonte
    size2=len(kenhlista)#epomenws to sinoliko megethos tis listas einai to athroisma olwn twn diasthmatwn pou exoun dwthei
    print 'To Athroismma tou mhkous twn diasthmatwn einai',size2

sumIntervals(lista)


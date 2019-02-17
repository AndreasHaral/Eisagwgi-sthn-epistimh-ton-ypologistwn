a=input("dwse lista")
max1 = 0#to megalitero max pou yparxei ekeini tin stigmi
athroisma =0#ena max pou yparxei ekeini tin stigmi
k=len(a)#size tou array pou edwse o xristis
start=0
end=0
for i in range(k): 
    athroisma  = athroisma  + a[i]
    if  athroisma < 0: #midenizei to athroisma  an einai arnhtiko
        athroisma = 0
        start=i+1#otan ginete arnhtiko ksekina apo ton epomeno arithmo epomenws o epomenos einai h arxh tou neou subarray
    elif (max1 < athroisma ):#an to teleuaitaio max-athroisma einai mikrotero tou megaliterou max tote dinete i timi tou teleutaioy max-athroisma sto megalitero max
        max1=athroisma  
        end=i+k-1#telos subarray
    if end>k or end==0:#an omws to end einai megalitero apo to size xrisimopoioyme deytero tipo gia na vroume to telos t subarray
        end=i
print(max1,a[start:end+1])


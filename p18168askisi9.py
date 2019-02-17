a =[-10,-23,-1,-10,10,-6,25,1,-25]
max_so_far = 0
max_ending_here = 0
size=8
start=0
end=0
for i in range(0, size): 
    max_ending_here = max_ending_here + a[i]
    if max_ending_here < 0: 
        max_ending_here = 0
        start=i+1#οταν γινεται αρνητικο ξεκινα απο τον επομενο αριθμο(Αρχη)
    elif (max_so_far < max_ending_here): 
        max_so_far = max_ending_here 
        end=i+size-1#τελος subarray
    if end>size or end==0:
        end=i
print(max_so_far,a[start:end+1])


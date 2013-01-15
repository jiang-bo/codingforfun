#!/usr/bin/python

def count_sort(array):
    max=0
    for a in array:
        if a >max:
            max=a
    count=[0]*(max+1)
    for a in array:
        count[a]+=1
    i=1
    while i<=max:
        count[i]=count[i]+count[i-1]    
        i+=1
    j=len(array)-1
    order=[0]*(len(array))
    while j>=0:
        order[count[array[j]]-1]=array[j]
        
        count[array[j]]-=1
        j-=1
    return order
        
print count_sort([3,1,2,7,1,9])
    
    
        
    
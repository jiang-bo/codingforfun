#!/usr/bin/python

def merge_sort(array):
    length=len(array)
    if(length<=1):
        return array

    m=length/2
    left=merge_sort(array[0:m])
    right=merge_sort(array[m:len(array)])
    
    result=[]
    l=0
    r=0
    while(l<len(left) and r<len(right)):
        if(left[l]<right[r]):
            result.append(left[l])
            l=l+1
        else:
            result.append(right[r])
            r=r+1
    while(l<len(left)):
        result.append(left[l])
        l=l+1
    while(r<len(right)):
        result.append(right[r])
        r=r+1
    return result

print merge_sort([1,3,10,2,1,7,5])
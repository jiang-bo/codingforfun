#!/usr/bin/python

def quick_sort(array):
    sort(array,0,len(array)-1)
    return array

def sort(array, left, right):
    if(left>=right):
        return
    mid=array[(left+right)/2]
    l=left
    r=right
    while(l<r):
        while(array[l]<mid and l<r):
            l+=1
        while(array[r]>=mid and r>l):
            r -= 1
        if(l<r):
            tmp=array[r]
            array[r]=array[l]
            array[l]=tmp
    
    sort(array,left, l)
    sort(array,r+1, right)

print quick_sort([3,0,9,8,2,10,7])
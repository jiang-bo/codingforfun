#!/usr/bin/python

def heap_sort(array):
    l=len(array)
    #heapfy
    i=1
    while(i<l):
        if(array[i]>array[i/2]):
            swap(array, i, i/2)
        i=i+1
    #shift
    t=l-1
    while(t>0):
        swap(array, 0,t)
        shiftdown(array,0,t-1)
        t=t-1
    return array


def swap(array, i,j):
    tmp=array[i]
    array[i]=array[j]
    array[j]=tmp

def shiftdown(array,t,e):
    while(2*t<=e):
        if((2*t+1>e and array[2*t]>array[t]) or (array[2*t]>array[2*t+1] and array[2*t]>array[t])):
            swap(array, t, 2*t)
            t=2*t
        elif(2*t+1<=e and array[2*t+1]>array[2*t] and array[2*t+1]>array[t]):
            swap(array, t,2*t+1)
            t=2*t+1
        else:
            return
    
print heap_sort([3,7,9,2,8,1,10])
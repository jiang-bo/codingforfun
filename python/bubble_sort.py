#!/usr/bin/python

def bubble_sort(array):
    l=len(array)
    i=0
    while (i<l):
        j=i
        while(j>0 and array[j]<array[j-1]):
            tmp=array[j]
            array[j]=array[j-1]
            array[j-1]=tmp
            j-=1
        i+=1


def test(array):
    print 'Source array:',array
    bubble_sort(array)
    print 'Sort array:',array


test([3,7,1,9,8,2,7,3,10])
# -*- coding: utf-8 -*-

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_array = [i for i in array[1:] if i <= pivot]
        greater_array = [i for i in array[1:] if i > pivot]
        return quicksort(less_array) + [pivot] + quicksort(greater_array)
    
print(quicksort([10,5,2,3]))
# -*- coding: utf-8 -*-

#practice 4.1
def sumArray(array):
    if array:
        return (array.pop() + sumArray(array))
    else:
        return 0

#practice 4.2
def countArray(array):
    if array:
        array.pop()
        return (1 + countArray(array))
    else:
        return 0

#practice 4.3
def findBiggest(array):
    if len(array) >= 2:
        biggest = array.pop()
        challenger = findBiggest(array)
        if biggest >= challenger:
            return biggest
        else:
            return challenger
    elif len(array) == 1:
        return array.pop()

input_array = [1,2,3,4,5]
print(sumArray(input_array))

input_array = [1,2,3,4,5]
print(countArray(input_array))

input_array = [5,4,3,2,1]
print(findBiggest(input_array))
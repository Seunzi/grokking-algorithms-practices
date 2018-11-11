# -*- coding: utf-8 -*-
import math

def binary_search(usr_list, usr_item):
    low = 0
    high = len(usr_list) - 1

    while low <= high:
        # the '/' come out with float type, no matter what the result is.
        # the '//' come out with int type, it removes everything after the decimal point.
        # using math.ceil() for rounded up the value, otherwise it will get None of the list's 2nd value
        mid = math.ceil((low + high) / 2)
        guess = usr_list[mid]
        if guess == usr_item:
            return mid
        if guess > mid:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,5))
print(binary_search(my_list,-1))
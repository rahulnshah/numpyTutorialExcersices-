# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:56:49 2022

@author: rahul
"""

import numpy as np 

arr = np.array([1,2,3,4,5])
# print(arr)

# Insert the correct syntax for printing the first item in the array.

first_element = arr[0]
# print(first_element)

"""Insert the correct slicing syntax to print the following selection of the array: 
Everything from (including) the second item to (not including) the fifth item."""

arr = np.array([10, 15, 20, 25, 30, 35, 40])
# print(arr[1:4])

# returns the data type of the array:
# print(arr.dtype)

# Use the correct method to make a copy of the array.
x = arr.copy()
x[0] = 20
# print(x)
# print(arr)

# Use the correct NumPy syntax to check the shape of an array.

arr = np.array([1, 2, 3, 4, 4])
# print(arr.shape)

# Use the correct NumPy method to change the shape of an array from 1-D to 2-D.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3,4)
arr[0] = 11
# print(newarr)

# iterate over the 5-dim array
arr = np.array([[[[[1,2,4,8]]]]])
"""for x in np.nditer(arr):
    print(x)"""
    
# Use a correct NumPy method to join two arrays into a single array.

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr3 = np.array([75, 9])

arr = np.concatenate((arr1, arr2, arr3))
# print(arr)

# Use the correct NumPy method to find all items with the value 4.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
# print(x)

# Give all numbers from arr greater than or equal to 2 
greater_than_or_equal_2 = arr[arr >= 2]
print(greater_than_or_equal_2)



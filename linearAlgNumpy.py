"""
@author: rahul
"""
import numpy as np
# Sums and Scalar Multiples 

a = np.array([[2,0,-1],[4,-5,2]])
b = np.array([[7,-5,1],[1,-4,-3]])

# A + B
# print(np.add(a,b))

# B - 2A
a_scalar = 2
c = np.subtract(b, np.multiply(a, a_scalar))
# print(c)

# A + 2B 
d = np.add(a, np.multiply(b, a_scalar))
# print(d)

# Matrix Multiplication 

# CB
c = np.array([[1,2],[3,4],[5,6]])
e = np.matmul(c,b)
# print(e)

# C(B+C)
c = np.subtract(b, np.multiply(a, a_scalar))
d = np.array([[1,2],[3,4],[5,6]])
f = np.matmul(d,np.add(b,c))
# print(f)

# The Transpose of a Matrix
g = np.array([[1,2,3,4],[2,3,4,5]])
# print('g\n',g)
g = np.transpose(g)
# print('g\n',g)
g = np.transpose(g)
# print('g\n',g)

a = np.transpose(g) # a and g are not aliases 
# print('a\n',a)
# print('g\n',g)


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

# Linear Transformations 
a = np.array([[1,-3],[3,5]])
u = np.array([2,-1])
b = np.array([3,2])
# a) Find T(u), the image of u under the transformation T . 
t_of_u = np.matmul(a,u)
print(t_of_u)

# b) Find an x in R^2 whose image under T is b
'''T(x) = Ax = b, so just solve for x, which is 
part of the domain of T in R^2'''

x = np.linalg.solve(a,b) 
# print('Coefficient Matrix')
# print(a)
# print('\nDependent Variable vector')
# print(b)
# print('\nSolution')
# print(x) 

# Find determinant of a 
det_of_a = np.linalg.det(a)
# print("determinant of a\n", det_of_a)
if det_of_a == 0:
    print("a is singular")
else:
    print("a is not singular")
    
# Example of a shear transformation T: R^2 -> R^2
sq_mat = np.array([[2,0],[0,2]])
u = np.array([1,-3])
t_of_u = np.matmul(sq_mat, u)
print("image under T of u:\n", t_of_u) 


'''Let T: R^2 -> R^2 be a linear transformation that maps
u D
#
5
2
$
into #
2
1
$
and maps v D
#
1
3
$
into #
"1
3
$
. Use the
fact that T is linear to find the images under T of 3u, 2v, and
3u C 2v.'''

'''Explanation:
    T(3u + 2v).  T(cu) = cT(u) T(u + v) = T(u) + T(v)
    = T(3u) + T(2v) = 3T(u) + 2T(v)'''
t_of_u = np.array([2,1])
t_of_v = np.array([-1,3])
t_of_3u_p_2v = np.add(np.multiply(t_of_u, 3),np.multiply(t_of_v, 2))
print("T(3u + 2v):\n", t_of_3u_p_2v)   
import numpy as np

a = np.array([1,2,3,4], ndmin=4)
print(a)
#result: array([[[[1, 2, 3, 4]]]])


b = np.array([1,2,3,4],dtype=complex)

print(b)

# result: [1.+0.j 2.+0.j 3.+0.j 4.+0.j]


# >>>>>>>>>>> array attributes >>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#--------------ndarray.shape-----------------------

c = np.array([[1,2,3],[4,5,6]])

print(c.shape)

#result : (2, 3)

c.shape=(3,2)

print(c)

#result
#array([[1, 2],
#       [3, 4],
#       [5, 6]])


#------------ ndarray.ndim ------------------------

import numpy as np 
d = np.arange(24)
print(d.ndim)
#result: 1


# 2 matrix 3 by 4
d.reshape(2,3,4)
print(d)

#result: 
#array([[[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]],

#       [[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]]])





















#<<<<<<<<<<<<< array attributes <<<<<<<<<<<<









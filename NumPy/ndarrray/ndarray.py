import numpy as np

a = np.array([1,2,3,4], ndmin=4)
print(a)
#result: array([[[[1, 2, 3, 4]]]])


b = np.array([1,2,3,4],dtype=complex)

print(b)

# result: [1.+0.j 2.+0.j 3.+0.j 4.+0.j]


#>>>>>>>>>>>>> structered array >>>>>>>>>>>>>>

#source: https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html

# Creating record arrays (numpy.rec)


# Character	Description	Example
#'b'	Byte	np.dtype('b')
#'i'	Signed integer	np.dtype('i4') == np.int32
#'u'	Unsigned integer	np.dtype('u1') == np.uint8
#'f'	Floating point	np.dtype('f8') == np.int64
#'c'	Complex floating point	np.dtype('c16') == np.complex128
#'S', 'a'	String	np.dtype('S5')
#'U'	Unicode string	np.dtype('U') == np.str_
#'V'	Raw data (void)	np.dtype('V') == np.void

import numpy as np
mystructeredtype = np.dtype({'names':('name', 'age', 'weight'),
          'formats':('U10', 'i4', 'f8')})

#or
# mystructeredtype = np.dtype({'names':('name', 'age', 'weight'),
# 'formats':((np.str_, 10), int, np.float32)})          

#or
# np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])

data = np.zeros(4,dtype=mystructeredtype)
names = ["murat","ali","mehmet","ahmet"]
ages=[30,45,32,23]
weights=[56. , 67. , 54. , 70.]

data["name"]=names
data["age"]=ages
data["weight"]=weights

print(data)
# result : [('murat', 30, 56.) ('ali', 45, 67.) ('mehmet', 32, 54.) ('ahmet', 23, 70.)]

print(data[0])
#result : [('murat', 30, 56.)]

print(data[-1]['name'])
#result : 'ahmet'


#>>>>>> More Advanced Compound Types >>>>>>>>>
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])

# result 
#(0, [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
#[[ 0.  0.  0.]
# [ 0.  0.  0.]
# [ 0.  0.  0.]]





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

#-------------ndarray.itemsize----------------------


# dtype of array is int8 (1 byte) 
import numpy as np 
e = np.array([1,2,3,4,5], dtype = np.int8) 
print(e.itemsize)

#result : 1


# dtype of array is now float32 (4 bytes) 
import numpy as np 
f = np.array([1,2,3,4,5], dtype = np.float32) 
print (f.itemsize)
# result: 4


#<<<<<<<<<<<<< array attributes <<<<<<<<<<<<









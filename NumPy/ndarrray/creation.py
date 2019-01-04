#>>>>>>>>>>>>>>>>>>>>>> numpy.empty >>>>>>>>>>>>>>>>>>>
# numpy.empty(shape, dtype = float, order = 'C')

import numpy as np
a = np.empty([3,2], dtype = int) 
print (a)

#result:
#[[481036337261 519691042932]
# [390842023976 188978561075]
# [399431958578 137438953516]]


#>>>>>>>>>>>>>>>>>>>>>>> numpy.zeros >>>>>>>>>>>>>>>>>>>

# numpy.zeros(shape, dtype = float, order = 'C')

import numpy as np 
b = np.zeros((2,2), dtype = np.int)  
print (b)

# result 
#[[0 0]
# [0 0]]        

#>>>>>>>>>>>>>>> numpy.ones >>>>>>>>>>>>>>>>>>>>>>>>>>>

import numpy as np
c = np.ones((2,2), dtype=np.int)

print(c)

#result : 
#[[1 1]
# [1 1]]


#>>>>>>>>>>>>>>>>>>>>>>>>>> numpy.random.randn >>>>>>>>>>>>>>>
#Return a sample (or samples) from the “standard normal” distribution.
# numpy.random.randn(d0, d1, ..., dn)

import numpy as np
d = np.random.randn(2,2)

print(d)

#result:
#[[-2.77180935  0.99742099]
# [-0.76309103 -0.33031291]]


#>>>>>>>>>>>>>>>>> ndarray from list and tuple >>>>>>>>>>>>>>>>

# convert list to ndarray 
import numpy as np 

e = [1,2,3]
# e = (1,2,3)
f = np.asarray(e) 
print (f)

#result:
#[1. 2. 3.]

#>>>>>>>>>>>>>>>>> ndarray from frombuffer >>>>>>>>>>>>>>>>>>
# numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)

#buffer:Any object that exposes buffer interface
#dtype: Data type of returned ndarray. Defaults to float
#count: The number of items to read, default -1 means all data
#offset:The starting position to read from. Default is 0
import numpy as np 
#In PY3, the default string type is unicode. The b is used to create and display bytestrings.
g = b'Hello World' 
h = np.frombuffer(g, dtype = 'S1') 
print (h)
#result : [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']


#>>>>>>>>>>>>>>>>>>>>>> numpy.fromiter >>>>>>>>>>>>>>>>>>>>>
# numpy.fromiter(iterable, dtype, count = -1)
#iterable : Any iterable object
#dtype : Data type of resultant array
#count : The number of items to be read from iterator. Default is -1 which means all data to be read

# source : https://nvie.com/posts/iterators-vs-generators/


# create list object using range function 
# obtain iterator object from list 
import numpy as np 
list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
i = np.fromiter(it, dtype = float) 
print (i)
# result: [0. 1. 2. 3. 4.]

iterable = (x*x for x in range(5))
f = np.fromiter(iterable, float)
print(f)
#result : array([0., 1., 4., 9., 16.])


#>>>>>>>>>>>>>>>>>>>>Creating record arrays (numpy.rec)>>>>>>>>>>>>>>>>
# sreates a structered array

import numpy as np
mystructeredtype = np.dtype({'names':('name', 'age', 'weight'),
          'formats':('U10', 'i4', 'f8')})
data = np.recarray(4,dtype=mystructeredtype)
names = ["murat","ali","mehmet","ahmet"]
ages=[30,45,32,23]
weights=[56. , 67. , 54. , 70.]

data["name"]=names
data["age"]=ages
data["weight"]=weights

print(data.name)

# fields can be accessed as attributes rather than as dictionary keys
# result : array(['murat', 'ali', 'mehmet', 'ahmet'], dtype='<U10')


#>>>>>>>>>>>>>>>>>>>< Numarical Ranges >>>>>>>>>>>>>>>>>>>>>>>

#### Numerical ranges
# arange([start,] stop[, step,][, dtype])	Return evenly spaced values within a given interval.
# linspace(start, stop[, num, endpoint, …])	Return evenly spaced numbers over a specified interval.
# logspace(start, stop[, num, endpoint, base, …])	Return numbers spaced evenly on a log scale.
# geomspace(start, stop[, num, endpoint, dtype])	Return numbers spaced evenly on a - log scale (a geometric progression).
# meshgrid(*xi, **kwargs)	Return coordinate matrices from coordinate vectors.
# mgrid	nd_grid instance which returns a dense multi-dimensional “meshgrid”.
# ogrid	nd_grid instance which returns an open multi-dimensional “meshgrid”.

#>>>>>>>>>>>>>>>>>>> numpy.arange([start, ]stop, [step, ]dtype=None) >>>>>>>>>

import numpy as np

mydtype = np.float

# mydtype = 'f'

j = np.arange(0,10, 1, dtype=mydtype)

print(j)

# result : [0 1 2 3 4 5 6 7 8 9]

# >>>>>>>>>>>>>>>>>>>> numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) >>>>>>>>>>>>>>>>>>>>>>
# retstep : bool, optional
# If True, return (samples, step), where step is the spacing between samples.

import numpy as np
k = np.linspace(2.0, 3.0, num=5)
print(k)

# source : [2.   2.25 2.5  2.75 3.  ]

#>>>>>>>>>>>>>><numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)>>>>>>>>>
# https://docs.scipy.org/doc/numpy-1.15.4/reference/generated/numpy.logspace.html#numpy.logspace

# >>>>>>>>>>>>>> numpy.geomspace(start, stop, num=50, endpoint=True, dtype=None) >>>>>>>>>>>>>>>>>
# https://docs.scipy.org/doc/numpy-1.15.4/reference/generated/numpy.geomspace.html#numpy.geomspace


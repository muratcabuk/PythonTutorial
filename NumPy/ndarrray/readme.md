## ndarray

The most important object defined in NumPy is an N-dimensional array type called ndarray. It describes the collection of items of the same type. Items in the collection can be accessed using a zero-based index.

Every item in an ndarray takes the same size of block in the memory. Each element in ndarray is an object of data-type object (called dtype).

``` python
import numpy as np

# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#object : Any object exposing the array interface method returns an array, or any (nested) sequence.
#dtype : Desired data type of array, optional
#copy : Optional. By default (true), the object is copied
#order : C (row major) or F (column major) or A (any) (default)
#subok : By default, returned array forced to be a base class array. If true, sub-classes passed through
#ndmin : Specifies minimum dimensions of resultant array

```
#### Examples

``` python

import numpy as np

a = np.array([1,2,3,4], ndmin=4)
print(a)
#result: array([[[[1, 2, 3, 4]]]])


b = np.array([1,2,3,4],dtype=complex)

print(b)

# result: [1.+0.j 2.+0.j 3.+0.j 4.+0.j]

```

- #### ndarray.shape : This array attribute returns a tuple consisting of array dimensions. It can also be used to resize the array.

[good explanation](https://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html)


``` python

c = np.array([[1,2,3],[4,5,6]])

print(c.shape)

#result : (2, 3)

c.shape=(3,2)

print(c)

#result
#array([[1, 2],
#       [3, 4],
#       [5, 6]])

```
- ndarray.ndim: the number of axes (dimensions) of the array. This array attribute returns the number of array dimensions.
  
``` python
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

```
- ndarray.itemsize: the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.

``` python

# dtype of array is int8 (1 byte) 
import numpy as np 
e = np.array([1,2,3,4,5], dtype = np.int8) 
print (e.itemsize)

```

## Creation

### numpy.empty

numpy.empty(shape, dtype = float, order = 'C')

- Shape: Shape of an empty array in int or tuple of int
- Dtype: Desired output data type. Optional
- Order : 'C' for C-style row-major array, 'F' for FORTRAN style column-major array


``` python
numpy.empty(shape, dtype = float, order = 'C')

```
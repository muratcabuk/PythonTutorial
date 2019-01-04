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


### [Array creation routines](https://docs.scipy.org/doc/numpy-1.15.0/reference/routines.array-creation.html)

#### Ones and zeros

- empty(shape[, dtype, order])	Return a new array of given shape and type, without initializing entries.
- empty_like(prototype[, dtype, order, subok])	Return a new array with the same shape and type as a given array.
- eye(N[, M, k, dtype, order])	Return a 2-D array with ones on the diagonal and zeros elsewhere.
- identity(n[, dtype])	Return the identity array.
- ones(shape[, dtype, order])	Return a new array of given shape and type, filled with ones.
- ones_like(a[, dtype, order, subok])	Return an array of ones with the same shape and type as a given array.
- zeros(shape[, dtype, order])	Return a new array of given shape and type, filled with zeros.
 -zeros_like(a[, dtype, order, subok])	Return an array of zeros with the same shape and type as a given array.
- full(shape, fill_value[, dtype, order])	Return a new array of given shape and type, filled with fill_value.
- full_like(a, fill_value[, dtype, order, subok])	Return a full array with the same shape and type as a given array.

### From existing data
- array(object[, dtype, copy, order, subok, ndmin])	Create an array.
- asarray(a[, dtype, order])	Convert the input to an array.
- asanyarray(a[, dtype, order])	Convert the input to an ndarray, but pass ndarray subclasses through.
- ascontiguousarray(a[, dtype])	Return a contiguous array in memory (C order).
- asmatrix(data[, dtype])	Interpret the input as a matrix.
- copy(a[, order])	Return an array copy of the given object.
- frombuffer(buffer[, dtype, count, offset])	Interpret a buffer as a 1-dimensional array.
- fromfile(file[, dtype, count, sep])	Construct an array from data in a text or binary file.
- fromfunction(function, shape, **kwargs)	Construct an array by executing a function over each coordinate.
- fromiter(iterable, dtype[, count])	Create a new 1-dimensional array from an iterable object.
- fromstring(string[, dtype, count, sep])	A new 1-D array - initialized from text data in a string.
- loadtxt(fname[, dtype, comments, delimiter, …])	Load data from a text file.

#### Creating record arrays (numpy.rec)

[Structered Array](https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html)

Note: numpy.rec is the preferred alias for numpy.core.records.

- core.records.array(obj[, dtype, shape, …])	Construct a record array from a wide-variety of objects.
- core.records.fromarrays(arrayList[, dtype, …])	create a record array from a (flat) list of arrays
- core.records.fromrecords(recList[, dtype, …])	create a recarray from a list of records in text form
- core.records.fromstring(datastring[, dtype, …])	create a (read-only) record array from binary data contained in
- core.records.fromfile(fd[, dtype, shape, …])	Create an array from binary file data


#### Creating character arrays (numpy.char)
Note: numpy.char is the preferred alias for numpy.core.defchararray.

- core.defchararray.array(obj[, itemsize, …])	Create a chararray.
- core.defchararray.asarray(obj[, itemsize, …])	Convert the input to a chararray, copying the data only if necessary.

#### Numerical ranges
- arange([start,] stop[, step,][, dtype])	Return evenly spaced values within a given interval.
- linspace(start, stop[, num, endpoint, …])	Return evenly spaced numbers over a specified interval.
- logspace(start, stop[, num, endpoint, base, …])	Return numbers spaced evenly on a log scale.
- geomspace(start, stop[, num, endpoint, dtype])	Return numbers spaced evenly on a - log scale (a geometric progression).
- meshgrid(*xi, **kwargs)	Return coordinate matrices from coordinate vectors.
- mgrid	nd_grid instance which returns a dense multi-dimensional “meshgrid”.
- ogrid	nd_grid instance which returns an open multi-dimensional “meshgrid”.


#### Building matrices
- diag(v[, k])	Extract a diagonal or construct a diagonal array.
- diagflat(v[, k])	Create a two-dimensional array with the flattened input as a diagonal.
- tri(N[, M, k, dtype])	An array with ones at and below the given diagonal and zeros elsewhere.
- tril(m[, k])	Lower triangle of an array.
- triu(m[, k])	Upper triangle of an array.
- vander(x[, N, increasing])	Generate a Vandermonde matrix.


#### The Matrix class
- mat(data[, dtype])	Interpret the input as a matrix.
- bmat(obj[, ldict, gdict])	Build a matrix object from a string, nested sequence, or array. -->


### numpy.empty

numpy.empty(shape, dtype = float, order = 'C')

- Shape: Shape of an empty array in int or tuple of int
- Dtype: Desired output data type. Optional
- Order : 'C' for C-style row-major array, 'F' for FORTRAN style column-major array


``` python
numpy.empty(shape, dtype = float, order = 'C')

```






### RecordArray

NumPy also provides the np.recarray class, which is almost identical to the structured arrays just described, but with one additional feature: fields can be accessed as attributes rather than as dictionary keys. Recall that we previously accessed the ages by writing:
[source](https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html)

``` python

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

```
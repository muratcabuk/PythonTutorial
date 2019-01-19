### Matrix library (numpy.matlib)
This module contains all functions in the numpy namespace, with the following replacement functions that return matrices instead of ndarrays.

Functions that are also in the numpy namespace and return matrices

- mat(data[, dtype])	Interpret the input as a matrix.

numpy.mat(data, dtype=None)

``` python
x = np.array([[1, 2], [3, 4]])
m = np.asmatrix(x)
x[0,0] = 5
print(m)

# result : matrix([[5, 2],
#                  [3, 4]])




```



- matrix(data[, dtype, copy])	
Note :   It is no longer recommended to use this class, even for linear

class numpy.matrix(data, dtype=None, copy=True)
  
[see details](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.matrix.html#numpy.matrix) 


Attributes:	
A :Return self as an ndarray object.

A1 :Return self as a flattened ndarray.

H :Returns the (complex) conjugate transpose of self.

I :Returns the (multiplicative) inverse of invertible self.

T :Returns the transpose of the matrix.

``` python

a = np.matrix([[1, 2], [3, 4]])
print(a)
# result :matrix([[1, 2],
#         [3, 4]])

print(a.T)

#matrix([[1, 3],
#        [2, 4]])


```




- asmatrix(data[, dtype])	Interpret the input as a matrix.
- bmat(obj[, ldict, gdict])	Build a matrix object from a string, nested sequence, or array.


``` python
A = np.mat('1 1; 1 1')
B = np.mat('2 2; 2 2')
C = np.mat('3 4; 5 6')
D = np.mat('7 8; 9 0')

np.bmat([[A, B], [C, D]])
# result :matrix([[1, 1, 2, 2],
#        [1, 1, 2, 2],
#        [3, 4, 7, 8],
#        [5, 6, 9, 0]])
np.bmat(np.r_[np.c_[A, B], np.c_[C, D]])
#result :matrix([[1, 1, 2, 2],
#        [1, 1, 2, 2],
#        [3, 4, 7, 8],
#        [5, 6, 9, 0]])
np.bmat('A,B; C,D')
#result : matrix([[1, 1, 2, 2],
#        [1, 1, 2, 2],
#        [3, 4, 7, 8],
#        [5, 6, 9, 0]])






```




#### Replacement functions in matlib

- empty(shape[, dtype, order])	Return a new matrix of given shape and type, without initializing entries.
- zeros(shape[, dtype, order])	Return a matrix of given shape and type, filled with zeros.
- ones(shape[, dtype, order])	Matrix of ones.
- eye(n[, M, k, dtype, order])	Return a matrix with ones on the diagonal and zeros elsewhere.
- identity(n[, dtype])	Returns the square identity matrix of given size.
- repmat(a, m, n)	Repeat a 0-D to 2-D array or matrix MxN times.

``` python

a1 = np.arange(4)
np.matlib.repmat(a1, 2, 2)
# result : array([[0, 1, 2, 3, 0, 1, 2, 3],
#       [0, 1, 2, 3, 0, 1, 2, 3]])



```



- rand(*args)	Return a matrix of random values with given shape.
- randn(*args)	Return a random matrix with data from the “standard normal” distribution.
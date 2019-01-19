### Linear algebra (numpy.linalg)


[SciPy Linalg Library](https://docs.scipy.org/doc/scipy-0.13.0/reference/linalg.html)




#### Matrix and vector products
- dot(a, b[, out])	Dot product of two arrays.


Dot product of two arrays. Specifically,

    - If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).

    - If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.

    - If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.

    - If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.

    - If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:

    - dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])

``` python
a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
np.dot(a, b)
# result : array([[4, 1],
#       [2, 2]])

# if a and b would are matrix 
c= np.asmatrix(a)
d = np.asmatrix(b)
a*b
# result
#array([[4, 0],
#       [0, 2]])


```





- linalg.multi_dot(arrays)	Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order.

``` python

from numpy.linalg import multi_dot
# Prepare some data
A = np.random.random((10000, 100))
B = np.random.random((100, 1000))
C = np.random.random((1000, 5))
D = np.random.random((5, 333))
# the actual dot multiplication
_ = multi_dot([A, B, C, D])
# instead of:


_ = np.dot(np.dot(np.dot(A, B), C), D) 
# or >>> _ = A.dot(B).dot(C).dot(D) …




```





- vdot(a, b)	Return the dot product of two vectors.

Note that vdot handles multidimensional arrays differently than dot: it does not perform a matrix product, but flattens input arguments to 1-D vectors first. Consequently, it should only be used for vectors.

``` python

a = np.array([[1, 4], [5, 6]])
b = np.array([[4, 1], [2, 2]])
np.vdot(a, b)
# result : 30
np.vdot(b, a)
# result : 30
1*4 + 4*1 + 5*2 + 6*2
# result 30



```



- inner(a, b)	Inner product of two arrays.
Ordinary inner product of vectors for 1-D arrays (without complex conjugation), in higher dimensions a sum product over the last axes.

For vectors (1-D arrays) it computes the ordinary inner-product:

np.inner(a, b) = sum(a[:]*b[:])

More generally, if ndim(a) = r > 0 and ndim(b) = s > 0:

np.inner(a, b) = np.tensordot(a, b, axes=(-1,-1))

or explicitly:

np.inner(a, b)[i0,...,ir-1,j0,...,js-1]
     = sum(a[i0,...,ir-1,:]*b[j0,...,js-1,:])
In addition a or b may be scalars, in which case:

np.inner(a,b) = a*b



``` python

a = np.array([1,2,3])
b = np.array([0,1,0])
np.inner(a, b)
# result : 2


```

- outer(a, b[, out])	Compute the outer product of two vectors.

Compute the outer product of two vectors.

Given two vectors, a = [a0, a1, ..., aM] and b = [b0, b1, ..., bN], the outer product [1] is:

[[a0*b0  a0*b1 ... a0*bN ]

 [a1*b0    .

 [ ...          .

 [aM*b0            aM*bN ]]

``` python
x = np.array(['a', 'b', 'c'], dtype=object)
np.outer(x, [1, 2, 3])
#result : array([[a, aa, aaa],
#                [b, bb, bbb],
#                [c, cc, ccc]], dtype=object)



```

__inner vs outer vs dot__


``` python
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[6,5,4],[3,2,1]])
np.outer(a,b)

# result 
#array([[ 6,  5,  4,  3,  2,  1],
#       [12, 10,  8,  6,  4,  2],
#       [18, 15, 12,  9,  6,  3],
#       [24, 20, 16, 12,  8,  4],
#       [30, 25, 20, 15, 10,  5],
#       [36, 30, 24, 18, 12,  6]])

np.inner(a,b)

#result
#array([[28, 10],
#       [73, 28]])


np.dot(a,b)

# result : ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)



```







- matmul(a, b[, out])	Matrix product of two arrays.

Matrix product of two arrays.

The behavior depends on the arguments in the following way.

    If both arguments are 2-D they are multiplied like conventional matrices.
    If either argument is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly.
    If the first argument is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed.
    If the second argument is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed.


``` python
# For 2-D arrays it is the matrix product:


a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.matmul(a, b)
#result : array([[4, 1],
#                [2, 2]])

# For 2-D mixed with 1-D, the result is the usual.

a = [[1, 0], [0, 1]]
b = [1, 2]
np.matmul(a, b)
# array([1, 2])
np.matmul(b, a)
# array([1, 2])



```



- tensordot(a, b[, axes])	Compute tensor dot product along specified axes for arrays >= 1-D.

[Tensor Means](http://www.wikizeroo.net/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvVGVuc29y)

[Video Tutorial](https://www.youtube.com/watch?v=f5liqUk0ZTw)

[Video Tutorial 2](https://www.youtube.com/watch?v=CliW7kSxxWU)

``` python

# TODO: I will add example after study tensor


```



- einsum(subscripts, *operands[, out, dtype, …])	Evaluates the Einstein summation convention on the operands.


- einsum_path(subscripts, *operands[, optimize])	Evaluates the lowest cost contraction order for an einsum expression by considering the creation of intermediate arrays.


- linalg.matrix_power(a, n)	Raise a square matrix to the (integer) power n.


- kron(a, b)	Kronecker product of two arrays.

Turkish Note: rastgele boyutlarda iki matrisin blok matris olusturacak sekilde carpilmasini saglayan, bir nevi tensor carpimi.



#### Decompositions (or Factorization)

A matrix decomposition is a way of reducing a matrix into its constituent parts.

[Wikipedia](http://www.wikizeroo.net/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTWF0cml4X2RlY29tcG9zaXRpb24)

[Intro](https://machinelearningmastery.com/introduction-to-matrix-decompositions-for-machine-learning/)



- linalg.cholesky(a)	Cholesky decomposition.
- linalg.qr(a[, mode])	Compute the qr factorization of a matrix.
- linalg.svd(a[, full_matrices, compute_uv])	Singular Value Decomposition.
#### Matrix eigenvalues
- linalg.eig(a)	Compute the eigenvalues and right eigenvectors of a square array.
- linalg.eigh(a[, UPLO])	Return the eigenvalues and eigenvectors of a Hermitian or symmetric matrix.
- linalg.eigvals(a)	Compute the eigenvalues of a general matrix.
- linalg.eigvalsh(a[, UPLO])	Compute the eigenvalues of a Hermitian or real symmetric matrix.
#### Norms and other numbers
- linalg.norm(x[, ord, axis, keepdims])	Matrix or vector norm.
- linalg.cond(x[, p])	Compute the condition number of a matrix.
- linalg.det(a)	Compute the determinant of an array.
- linalg.matrix_rank(M[, tol, hermitian])	Return matrix rank of array using SVD method
- linalg.slogdet(a)	Compute the sign and (natural) logarithm of the determinant of an array.
- trace(a[, offset, axis1, axis2, dtype, out])	Return the sum along diagonals of the array.
#### Solving equations and inverting matrices
- linalg.solve(a, b)	Solve a linear matrix equation, or system of linear scalar equations.
- linalg.tensorsolve(a, b[, axes])	Solve the tensor equation a x = b for x.
- linalg.lstsq(a, b[, rcond])	Return the least-squares solution to a linear matrix equation.
- linalg.inv(a)	Compute the (multiplicative) inverse of a matrix.
- linalg.pinv(a[, rcond])	Compute the (Moore-Penrose) pseudo-inverse of a matrix.
- linalg.tensorinv(a[, ind])	Compute the ‘inverse’ of an N-dimensional array.
Exceptions
- linalg.LinAlgError	Generic Python-exception-derived object raised by linalg functions.
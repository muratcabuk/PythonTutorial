### Binary operations
####  Elementwise bit operations
- bitwise_and(x1, x2, /[, out, where, …])	Compute the bit-wise AND of two arrays element-wise.


numpy.bitwise_and(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'bitwise_and'>

Parameters:	x1, x2 : array_like
- Only integer and boolean types are handled.

- out : ndarray, None, or tuple of ndarray and None, optional
A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

- where : array_like, optional
Values of True indicate to calculate the ufunc at that position, values of False indicate to leave the value in the output alone.

- **kwargs
For other keyword-only arguments, see the ufunc docs.

Returns: out : ndarray or scalar
- Result. This is a scalar if both x1 and x2 are scalars.


``` python
# The number 13 is represented by 00001101. Likewise, 17 is represented by 00010001. The bit-wise AND of 13 and 17 is therefore 000000001, or 1:

print (np.bitwise_and(13, 17))

# result : 1


np.binary_repr(12)
# result : '1100'

np.bitwise_and([14,3], 13)
#result : array([12,  1])


```




- bitwise_or(x1, x2, /[, out, where, casting, …])	Compute the bit-wise OR of two arrays element-wise.
- bitwise_xor(x1, x2, /[, out, where, …])	Compute the bit-wise XOR of two arrays element-wise.
- invert(x, /[, out, where, casting, order, …])	Compute bit-wise inversion, or bit-wise NOT, element-wise.
- left_shift(x1, x2, /[, out, where, casting, …])	Shift the bits of an integer to the left.
- right_shift(x1, x2, /[, out, where, …])	Shift the bits of an integer to the right.
#### Bit packing
- packbits(myarray[, axis])	Packs the elements of a binary-valued array into bits in a uint8 array.
- unpackbits(myarray[, axis])	Unpacks elements of a uint8 array into a binary-valued output array.
#### Output formatting
- binary_repr(num[, width])	Return the binary representation of the input number as a string.
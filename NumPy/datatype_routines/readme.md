### Scalars
Python defines only one type of a particular data class (there is only one integer type, one floating-point type, etc.). This can be convenient in applications that don’t need to be concerned with all the ways data can be represented in a computer. For scientific computing, however, more control is often needed.

In NumPy, there are 24 new fundamental Python types to describe different types of scalars. These type descriptors are mostly based on the types available in the C language that CPython is written in, with several additional types compatible with Python’s types.

Array scalars have the same attributes and methods as ndarrays. This allows one to treat items of an array partly on the same footing as arrays, smoothing out rough edges that result when mixing scalar and array operations.

Array scalars live in a hierarchy (see the Figure below) of data types. They can be detected using the hierarchy: For example, isinstance(val, np.generic) will return True if val is an array scalar object. Alternatively, what kind of array scalar is present can be determined using other members of the data type hierarchy. Thus, for example isinstance(val, np.complexfloating) will return True if val is a complex valued type, while isinstance(val, np.flexible) will return true if val is one of the flexible itemsize array types (string, unicode, void).

![dtypes](dtype-hierarchy.png)




#### Data type routines¶
- can_cast(from_, to[, casting])	Returns True if cast between data types can occur according to the casting rule.
numpy.can_cast(from_, to, casting='safe')


casting : {‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional
Controls what kind of data casting may occur.

- ‘no’ means the data types should not be cast at all.
- ‘equiv’ means only byte-order changes are allowed.
- ‘safe’ means only casts which can preserve values are allowed.
- ‘same_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
- ‘unsafe’ means any data conversions may be done.



``` python

np.can_cast(np.float64, complex)
#result : True

np.can_cast(complex, float)
#result : False

np.can_cast('i8', 'f8')
# result : True

np.can_cast('i8', 'f4')
#result : False


# Casting scalars
np.can_cast(100, 'i1')
# True
np.can_cast(150, 'i1')
# False

#Array scalar checks the value, array does not
np.can_cast(np.array(1000.0), np.float32)
# True
np.can_cast(np.array([1000.0]), np.float32)
# False

#Using the casting rules

np.can_cast('i8', 'i8', 'no')
#True
np.can_cast('<i8', '>i8', 'no')
#False
np.can_cast('<i8', '>i8', 'equiv')
#True
np.can_cast('<i4', '>i8', 'equiv')
#False
np.can_cast('<i4', '>i8', 'safe')
#True
np.can_cast('<i8', '>i4', 'safe')
#False
np.can_cast('<i8', '>i4', 'same_kind')
#True
np.can_cast('<i8', '>u4', 'same_kind')
#False
np.can_cast('<i8', '>u4', 'unsafe')
#True











```





- promote_types(type1, type2)	Returns the data type with the smallest size and smallest scalar kind to which both type1 and type2 may be safely cast.
- min_scalar_type(a)	For scalar a, returns the data type with the smallest size and smallest scalar kind which can hold its value.
- result_type(*arrays_and_dtypes)	Returns the type that results from applying the NumPy type promotion rules to the arguments.
- common_type(*arrays)	Return a scalar type which is common to the input arrays.
- obj2sctype(rep[, default])	Return the scalar dtype or NumPy equivalent of Python type of an object.
#### Creating data types
- dtype(obj[, align, copy])	Create a data type object.
- format_parser(formats, names, titles[, …])	Class to convert formats, names, titles description to a dtype.
#### Data type information
- finfo(dtype)	Machine limits for floating point types.
- iinfo(type)	Machine limits for integer types.
- MachAr([float_conv, int_conv, …])	Diagnosing machine parameters.
#### Data type testing
- issctype(rep)	Determines whether the given object represents a scalar data-type.


Parameters:	
rep : any
If rep is an instance of a scalar dtype, True is returned. If not, False is returned.

``` python
np.issctype(np.int32)
#True
np.issctype(list)
#False
np.issctype(1.1)
#False





```
- issubdtype(arg1, arg2)	Returns True if first argument is a typecode lower/equal in type hierarchy.

``` python
typechars = ['S1', '?', 'B', 'D', 'G', 'F', 'I', 'H', 'L', 'O', 'Q',
...              'S', 'U', 'V', 'b', 'd', 'g', 'f', 'i', 'h', 'l', 'q']
for typechar in typechars:
     print(typechar, ' : ', np.typename(typechar))

# result :
#S1  :  character
#?  :  bool
#B  :  unsigned char
#D  :  complex double precision
#G  :  complex long double precision
#F  :  complex single precision
#I  :  unsigned integer
#H  :  unsigned short
#L  :  unsigned long integer
#O  :  object
#Q  :  unsigned long long integer
#S  :  string
#U  :  unicode
#V  :  void
#b  :  signed char
#d  :  double precision
#g  :  long precision
#f  :  single precision
#i  :  integer
#h  :  short
#l  :  long integer
#q  :  long long integer




```





- issubsctype(arg1, arg2)	Determine if the first argument is a subclass of the second argument.
- issubclass_(arg1, arg2)	Determine if a class is a subclass of a second class.
- find_common_type(array_types, scalar_types)	Determine common type following standard coercion rules.
#### Miscellaneous
- typename(char)	Return a description for the given data type code.
- sctype2char(sctype)	Return the string representation of a scalar dtype.
- mintypecode(typechars[, typeset, default])	Return the character for the minimum-size type to which given types can be safely cast.

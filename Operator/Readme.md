### source : https://docs.python.org/3/library/operator.html#module-operator
### source : https://docs.python.org/3/howto/sorting.html#sortinghowto

# Introduction


The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y. Many function names are those used for special methods, without the double underscores. For backward compatibility, many of these have a variant with the double underscores kept. The variants without the double underscores are preferred for clarity.

The functions fall into categories that perform object comparisons, logical operations, mathematical operations and sequence operations.

|Operation   	        |Syntax	            |Function|
|-----------------------|-------------------|--------|
|Addition    	        |a + b	            |add(a, b)|
|Concatenation   	    |seq1 + seq2	    |concat(seq1, seq2)|
|Containment Test	    |obj in seq	        |contains(seq, obj)|
|Division	            |a / b	            |truediv(a, b)|
|Division	            |a // b	            |floordiv(a, b)|
|Bitwise And	        |a & b	            |and_(a, b)|
|Bitwise Exclusive Or	|a ^ b	            |xor(a, b)|
|Bitwise Inversion	    |~ a	            |invert(a)|
|Bitwise Or	            |a | b	            |or_(a, b)|
|Exponentiation	        |a ** b	            |pow(a, b)|
|Identity	            |a is b	            |is_(a, b)|
|Identity	            |a is not b	        |is_not(a, b)|
|Indexed Assignment	    |obj[k] = v	        |setitem(obj, k, v)|
|Indexed Deletion	    |del obj[k]	        |delitem(obj, k)|
|Indexing	            |obj[k]	            |getitem(obj, k)|
|Left Shift	            |a << b	            |lshift(a, b)|
|Modulo	                |a % b	            |mod(a, b)|
|Multiplication	        |a * b	            |mul(a, b)|
|Matrix Multiplication	|a @ b	            |matmul(a, b)|
|Negation (Arithmetic)	|- a	            |neg(a)|
|Negation (Logical)	    |not a	            |not_(a)|
|Positive	            |+ a	            |pos(a)|
|Right Shift	        |a >> b 	        |rshift(a, b)|
|Slice Assignment	    |seq[i:j] = values	|setitem(seq, slice(i, j), values)|
|Slice Deletion	        |del seq[i:j]	    |delitem(seq, slice(i, j))|
|Slicing	            |seq[i:j]   	    |getitem(seq, slice(i, j))|
|String Formatting	    |s % obj	        |mod(s, obj)|
|Subtraction	        |a - b  	        |sub(a, b)|
|Truth Test	            |obj	            |truth(obj)|
|Ordering	            |a < b	            |lt(a, b)|
|Ordering	            |a <= b	            |le(a, b)|
|Equality	            |a == b	            |eq(a, b)|
|Difference	            |a != b	            |ne(a, b)|
|Ordering	            |a >= b	            |ge(a, b)|
|Ordering	            |a > b	            |gt(a, b)|



##attrgetter, itemgetter

operator.attrgetter(attr)
operator.attrgetter(*attrs)

Return a callable object that fetches attr from its operand. If more than one attribute is requested, returns a tuple of attributes. The attribute names can also contain dots. For example:

After f = attrgetter('name'), the call f(b) returns b.name.
After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).


operator.itemgetter(item)
operator.itemgetter(*items)

Return a callable object that fetches item from its operand using the operand’s __getitem__() method. If multiple items are specified, returns a tuple of lookup values. For example:

After f = itemgetter(2), the call f(r) returns r[2].
After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).


    itemgetter(1)('ABCDEFG')
    # result: 'B'
    itemgetter(1,3,5)('ABCDEFG')
    # result : ('B', 'D', 'F')


## methodcaller

Return a callable object that calls the method name on its operand. If additional arguments and/or keyword arguments are given, they will be given to the method as well. For example:

After f = methodcaller('name'), the call f(b) returns b.name().
After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).


## Inplace Operators

Many operations have an “in-place” version. Listed below are functions providing a more primitive access to in-place operators than the usual syntax does; for example, the statement x += y is equivalent to x = operator.iadd(x, y). Another way to put it is to say that z = operator.iadd(x, y) is equivalent to the compound statement z = x; z += y.

In those examples, note that when an in-place method is called, the computation and assignment are performed in two separate steps. The in-place functions listed below only do the first step, calling the in-place method. The second step, assignment, is not handled.

operator.iadd(a, b)
operator.__iadd__(a, b)
a = iadd(a, b) is equivalent to a += b.

operator.iand(a, b)
operator.__iand__(a, b)
a = iand(a, b) is equivalent to a &= b.

operator.iconcat(a, b)
operator.__iconcat__(a, b)
a = iconcat(a, b) is equivalent to a += b for a and b sequences.

operator.ifloordiv(a, b)
operator.__ifloordiv__(a, b)
a = ifloordiv(a, b) is equivalent to a //= b.

operator.ilshift(a, b)
operator.__ilshift__(a, b)
a = ilshift(a, b) is equivalent to a <<= b.

operator.imod(a, b)
operator.__imod__(a, b)
a = imod(a, b) is equivalent to a %= b.

operator.imul(a, b)
operator.__imul__(a, b)
a = imul(a, b) is equivalent to a *= b.

operator.imatmul(a, b)
operator.__imatmul__(a, b)
a = imatmul(a, b) is equivalent to a @= b.

New in version 3.5.

operator.ior(a, b)
operator.__ior__(a, b)
a = ior(a, b) is equivalent to a |= b.

operator.ipow(a, b)
operator.__ipow__(a, b)
a = ipow(a, b) is equivalent to a **= b.

operator.irshift(a, b)
operator.__irshift__(a, b)
a = irshift(a, b) is equivalent to a >>= b.

operator.isub(a, b)
operator.__isub__(a, b)
a = isub(a, b) is equivalent to a -= b.

operator.itruediv(a, b)
operator.__itruediv__(a, b)
a = itruediv(a, b) is equivalent to a /= b.

operator.ixor(a, b)
operator.__ixor__(a, b)
a = ixor(a, b) is equivalent to a ^= b.
















getter

methodcaller
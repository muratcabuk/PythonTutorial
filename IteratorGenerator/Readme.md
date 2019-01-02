# Iterator

### Source: https://www.programiz.com/python-programming/iterator

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.


    # define a list
    my_list = [4, 7, 0, 3]

    # get an iterator using iter()
    my_iter = iter(my_list)

    ## iterate through it using next() 

    #prints 4
    print(next(my_iter))

    #prints 7
    print(next(my_iter))

    ## next(obj) is same as obj.__next__()

    #prints 0
    print(my_iter.__next__())

    #prints 3
    print(my_iter.__next__())

    ## This will raise error, no items left
    next(my_iter)


In fact the for loop can iterate over any iterable. Let's take a closer look at how the for loop is actually implemented in Python.

    for element in iterable:
        # do something with element
Is actually implemented as.

    # create an iterator object from that iterable
    iter_obj = iter(iterable)

    # infinite loop
    while True:
        try:
            # get the next item
            element = next(iter_obj)
            # do something with element
        except StopIteration:
            # if StopIteration is raised, break from loop
            break


    # Building Your Own Iterator in Python

    class PowTwo:
        """Class to implement an iterator
        of powers of two"""

        def __init__(self, max = 0):
            self.max = max

        def __iter__(self):
            self.n = 0
            return self

        def __next__(self):
            if self.n <= self.max:
                result = 2 ** self.n
                self.n += 1
                return result
            else:
                raise StopIteration



    a = PowTwo(4)
    i = iter(a)
    next(i)
    1
    next(i)
    2


# Generators

### Source: https://www.programiz.com/python-programming/generator

Generators simplifies creation of iterators. A generator is a function that produces a sequence of results instead of a single value.

    def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

    y = yrange(3)
    y
    <generator object yrange at 0x401f30>
    y.next()
    0
    y.next()
    1
    y.next()
    2


### source: https://www.programiz.com/python-programming/generator

Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.

The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that while list comprehension produces the entire list, generator expression produces one item at a time.

They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.


    # Initialize the list
    my_list = [1, 3, 6, 10]

    # square each term using list comprehension
    # Output: [1, 9, 36, 100]
    [x**2 for x in my_list]

    # same thing can be done using generator expression
    # Output: <generator object <genexpr> at 0x0000000002EBDAF8>
    (x**2 for x in my_list)




    # Intialize the list
    my_list = [1, 3, 6, 10]

    a = (x**2 for x in my_list)
    # Output: 1
    print(next(a))

    # Output: 9
    print(next(a))

    # Output: 36
    print(next(a))

    # Output: 100
    print(next(a))

# Itertools

### source : https://www.datacamp.com/community/tutorials/python-iterator-tutorial
### source : https://docs.python.org/3/library/itertools.html
### source : https://www.blog.pythonlibrary.org/2016/04/20/python-201-an-intro-to-itertools/


Itertools is an built-in Python module that contains functions to create iterators for efficient looping. In short, it provides a lot of interesting tools to work with iterators! Some keep providing values for an infinite range, hence they should only be accessed by functions or loops that actually stop calling for more values eventually.

# Infinite iterators: Count, Cycle and Repeat

## count()

Argument: start, [step]
Result: start, start+step, start+2*step, …
Example: count(10) --> 10 11 12 13 14 ...

Make an iterator that returns evenly spaced values starting with number start. Often used as an argument to map() to generate consecutive data points. Also used with zip() to add sequence numbers. Roughly equivalent to:

    def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step

Usage

    from itertools import count

    for i in count(10):
        if i > 20:
            break
        else:
            print(i)
    #output:
    .
    .
    .
    18
    19
    20

## cycle()

Argument: p
Result: p0, p1, … plast, p0, p1, …
Example: cycle('ABCD') --> A B C D A B C D ...

    def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element

Usage

    from itertools import cycle
    count = 0
    for item in cycle('XYZ'):
        if count > 7:
            break
        print(item)
        count += 1
    #output
    Y
    Z
    X
    Y
    Z
    X
    Y

## Repeat()

Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified. Used as argument to map() for invariant parameters to the called function. Also used with zip() to create an invariant part of a tuple record.

Roughly equivalent to:

    def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

Usage

    from itertools import 
    #pow func needs two parameters. range func creates firs parameters for pow func and repeat func repeats given number infinetely
    list(map(pow, range(10), repeat(2)))
    # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Usage

    from itertools import repeat
    repeat(5, 5)
    iterator = repeat(5, 5)
    next(iterator)
    5
    next(iterator)
    5
    .
    .

# Iterators terminating on the shortest input sequence: accumulate(), chain(), chain.from_iterable(), compress(),dropwhile(), filterfalse(), groupby(), islice(), starmap(), takewhile(), tee(), zip_longest()

## accumulate()

Argument: p [,func]
Result: p0, p0+p1, p0+p1+p2, …
Example: accumulate([1,2,3,4,5]) --> 1 3 6 10 15


Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument). If func is supplied, it should be a function of two arguments. 

Roughly equivalent to:

    def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total

Example

    from itertools import accumulate
    a = accumulate([1,2,3,4,5])
    next(a)
    #result : 1
    next(a)
    #result : 3

    print(list(r))
    #result:  [1, 3, 6, 10, 15]


Example

    import operator
    from itertools import accumulate
    print(list(accumulate(range(1, 5), operator.mul)))
    #result: [1, 2, 6, 24]


## chain()

Argument: p, q, …
Result: p0, p1, … plast, q0, q1, …
Example: chain('ABC', 'DEF') --> A B C D E F

Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted.

Roughly equivalent to:

    def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
    

Example

    from itertools import chain
    my_list = list(chain(['foo', 'bar'], cmd, numbers))
    print(my_list)
    #result: ['foo', 'bar', 'ls', '/some/dir', 0, 1, 2, 3, 4]


## Compress()

The compress sub-module is useful for filtering the first iterable with the second. This works by making the second iterable a list of Booleans (or ones and zeroes which amounts to the same thing). Here’s how it works:

    from itertools import compress
    letters = 'ABCDEFG'
    bools = [True, False, True, True, False]
    my_list = list(compress(letters, bools))
    print(my_list)
    #result: ['A', 'C', 'D']


## dropwhile()

Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element. 
There is a neat little iterator contained in itertools called dropwhile This fun little iterator will drop elements as long as the filter criteria is True. Because of this, you will not see any output from this iterator until the predicate becomes False.

Roughly equivalent to:

    def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x

Example

    from itertools import dropwhile
    my_list= list(dropwhile(lambda x: x<5, [1,4,6,4,1]))
    print(my_list)
    #result : [6, 4, 1]


## filterfalse(predicate, iterable)

The filterfalse function from itertools is very similar to dropwhile. However instead of dropping values that match True, filterfalse will only return those values that evaluated to False. 

    from itertools import filterfalse
    def greater_than_five(x):
        return x > 5 

    my_list = list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10]))
    print(my_list)
    #result [1, 2, 3]

## groupby(iterable, key=None)

The groupby iterator will return consecutive keys and groups from your iterable. This one is kind of hard to wrap your head around without seeing an example. 

The operation of groupby() is similar to the uniq filter in Unix. It generates a break or new group every time the value of the key function changes (which is why it is usually necessary to have sorted the data using the same key function). That behavior differs from SQL’s GROUP BY which aggregates common elements regardless of their input order.

Example

    from itertools import groupby
    from operator import itemgetter

    my_list = [(1,2,3,4),(1,2),("a","a","b"),("b","c","d")]
    for g, items in groupby(my_list, itemgetter(0)):
        print("=" * 20)
        print (g)
        print ("-" * 10)
        for i in items:
            print(i)
    
    #output: 
    ====================
    1
    ----------
    (1, 2, 3, 4)
    (1, 2)
    ====================
    a
    ----------
    ('a', 'a', 'b')
    ====================
    b
    ----------
    ('b', 'c', 'd')


## islice()

Argument: seq, [start,] stop [, step]
Result: elements from seq[start:stop:step]
Example: islice('ABCDEFG', 2, None) --> C D E F G
Example islice(iterable, start, stop[, step])

Make an iterator that returns selected elements from the iterable. If start is non-zero, then elements from the iterable are skipped until start is reached. Afterward, elements are returned consecutively unless step is set higher than one which results in items being skipped. If stop is None, then iteration continues until the iterator is exhausted, if at all; otherwise, it stops at the specified position. Unlike regular slicing, islice() does not support negative values for start, stop, or step. Can be used to extract related fields from data where the internal structure has been flattened (for example, a multi-line report may list a name field on every third line). 

Example

    from itertools import islice
    iterator = islice('123456', 4)
    next(iterator)
    #result : 1
    next(iterator)
    #result : 2
    next(iterator)
    #result : 3


Example
    from itertools import islice
    my_list = [1,("a","b"), "c", 2,3,4, [1,2,3]]
    iterator = islice(my_list, 1,4)
    myList = list(iterator)
    print(myList)
    #result : [('a', 'b'), 'c', 2]



## starmap(function, iterable)
The starmap tool will create an iterator that can compute using the function and iterable provided. As the documentation mentions, “the difference between map() and starmap() (see following examples) parallels the distinction between function(a,b) and function(*c).”


Example
    from itertools import starmap
    def add(a, b):
        return a+b

    for item in starmap(add, [(2,3), (4,5)]):
        print(item)

    # result: 5
    # result :9

Example


    print(list(map(lambda x,y:x+y, *[(2,3),(4,5)])))
    #result : [6, 8]

## takewhile(predicate, iterable)

takewhile will create an iterator that returns elements from the iterable only as long as our predicate or filter is True. Let’s try a simple example to see how it works:

    from itertools import takewhile
    print(list(takewhile(lambda x: x<5, [1,4,6,4,1])))
    #result: [1, 4]

## tee(iterable, n=2)

The tee tool will create *n* iterators from a single iterable. What this means is that you can create multiple iterators from one iterable. Let’s look at some explanatory code to how it works:


Example

    from itertools import tee
    data = 'ABCDE'
    iter1, iter2 = tee(data)
    for item in iter1:
        print(item)
    #result
    #A
    #B
    #C
    #D
    #E
    
    for item in iter2:
        print(item)

    #result
    #A
    #B
    #C
    #D
    #E

## zip_longest(*iterables, fillvalue=None)

The zip_longest iterator can be used to zip two iterables together. If the iterables don’t happen to be the same length, then you can also pass in a fillvalue. Let’s look at a silly example based on the documentation for this function:

Example

    from itertools import zip_longest
    for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
        print (item)
    # result
    #('A', 'x')
    #('B', 'y')
    #('C', 'BLANK')
    #('D', 'BLANK')



# Combinatoric iterators: product(), permutations(), combinations(), combinations_with_replacement(), product('ABCD', repeat=2), permutations('ABCD', 2), combinations('ABCD', 2), combinations_with_replacement('ABCD', 2)

## combinations(iterable, r) and combinations_with_replacement(iterable, r)
If you have the need to create combinations, Python has you covered with itertools.combinations. What combinations allows you to do is create an iterator from an iterable that is some length long. Let’s take a look:

Example

    from itertools import combinations
    list(combinations('WXYZ', 2))
    #result [('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]

The combinations_with_replacement with iterator is very similar to combinations. The only difference is that it will actually create combinations where elements do repeat. 

Example

    from itertools import combcombinations_with_replacementinations
    list(combinations_with_replacement('WXYZ', 2))
    #result [('W', 'W'),('W', 'X'), ('W', 'Y'), ('W', 'Z'),('X','X') ('X', 'Y'), ('X', 'Z'), ('Y','Y'),('Y', 'Z'),('X','Z')]


## permutations

The permutations sub-module of itertools will return successive r length permutations of elements from the iterable you give it. Much like the combinations function, permutations are emitted in lexicographic sort order.

    from itertools import permutations
    for item in permutations('WXYZ', 2):
        print(''.join(item))
    # result
    #WX
    #WY
    #WZ
    #XW
    #XY
    #XZ
    #YW
    #YX
    #YZ
    #ZW
    #ZX
    #ZY

## Product 

The itertools package has a neat little function for creating Cartesian products from a series of input iterables. Yes, that function is product.

Example:

    from itertools import product
    arrays = [(-1,1), (-3,3), (-5,5)]
    cp = list(product(*arrays))
    print(cp)
    # result: [(-1, -3, -5), (-1, -3, 5), (-1, 3, -5), (-1, 3, 5), (1, -3, -5), (1, -3, 5), (1, 3, -5), (1, 3, 5)]



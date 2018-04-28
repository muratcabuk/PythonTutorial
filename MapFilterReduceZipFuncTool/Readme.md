# Introduction
The map, filter, and reduce built-in functions are handy functions for processing sequences. These owe much to the world of functional programming languages. The idea is to take a small function you write and apply it to all the elements of a sequence. This saves you writing an explicit loop. The implicit loop within each of these functions may be faster than an explicit for or while loop.

# Lambda

The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created. Lambda functions are mainly used in combination with the functions filter(), map() and reduce(). The lambda feature was added to Python due to the demand from Lisp programmers. 

    def f (x): return x**2
    print f(8)
    # output: 64

    g = lambda x: x**2
    print g(8)
    # output: 64

source: https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/

# Map

### source : https://www.python-course.eu/lambda.php

The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the function func to all the elements of the sequence seq. Before Python3, map() used to return a list, where each element of the result list was the result of the function func applied on the corresponding element of the list or tuple "seq". With Python 3, map() returns an iterator. 

    r = map(func, seq)

Example

    def calculateSquare(n):
        return n*n

    numbers = (1, 2, 3, 4)
    result = map(calculateSquare, numbers)
    print(result)

# Filter

#source: https://www.programiz.com/python-programming/methods/built-in/filter

The filter() method constructs an iterator from elements of an iterable for which a function returns true.

In simple words, the filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not.

The syntax of filter() method is:

    filter(function, iterable)

example

list of alphabets
    alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

    function that filters vowels
        def filterVowels(alphabet):
            vowels = ['a', 'e', 'i', 'o', 'u']

            if(alphabet in vowels):
                return True
            else:
                return False

    filteredVowels = filter(filterVowels, alphabets)

    print('The filtered vowels are:')
    for vowel in filteredVowels:
        print(vowel)



when function is defined

    (element for element in iterable if function(element))


# Zip
The zip() function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.

    myList= [1,2,3,4,5]
    result = zip(myList[0::2],myList[1::2])
    print(list(result))
    #result = [(1, 2), (3, 4)]

    #example
    numberList = [1, 2, 3]
    strList = ['one', 'two', 'three']
    print(list(zip(numberList, strList)))



# FuncTools

### Source : https://docs.python.org/3/library/functools.html

The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.

[logo]: https://www.python-course.eu/images/reduce.png
[logo]: https://www.python-course.eu/images/reduce_diagram.png


## Reduce
see example
## Sorted
see example
## Partial
see example
### source: https://www.techrepublic.com/article/partial-function-application-in-python/

Partial application allows you to bind one of the inputs of a function to a constant value, and create a new function that takes only the remaining operations, and keeps the bound input the same among all calls. The following is a simple example which uses the partial function from the functools module with the add function from the operator module, which works in the same way as the "+" operator but can be used as an object.

    from functools import *
    from operator import *
    add(1,2)

    add1 = partial(add, 1)
    add1(2)

    add1(10)

# @functools.lru_cache

LRU (least recently used) cache : http://www.wiki-zero.com/index.php?q=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvQ2FjaGVfYWxnb3JpdGhtcyNMZWFzdF9yZWNlbnRseV91c2VkXyhMUlUp

Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

simple example

    from functools import lru_cache

    @lru_cache(maxsize=32)
    def sum(n):
        print(n)
        return n + 1

    sum(1)
    #output: 1
             2
    sum(1)
    #output: 1



example
    from functools import lru_cache

    @lru_cache(maxsize=32)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    print([fib(n) for n in range(10)])
    #output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

We can easily uncache the return values as well by using:

    fib.cache_clear()
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

#source : https://www.python-course.eu/lambda.php

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

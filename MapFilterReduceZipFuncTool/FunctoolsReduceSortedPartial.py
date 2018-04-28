import functools

#---------------------Reduce----------------------

#https://www.python-course.eu/python3_lambda.php
#https://docs.python.org/3/library/functools.html

#simple example

def reduceFunc(a,b):
    return a*b

myList = [1,2,3,4]
result1 = functools.reduce(reduceFunc,myList)
print(result1)
#result: 24


#example

result2 = functools.reduce((lambda x,y:x*y), myList)
print(result2)
#result: 24


#---------------------Sorted----------------------
myList2 = [1,4,2,3,'e','r','f','a','i','u',4,8,9]

#sort strings
print(sorted([t for t in myList2 if type(t)==str]))
#result : ['a', 'e', 'f', 'i', 'r', 'u']

#sort numbers
print(sorted([t for t in myList2 if type(t)==int]))
#result : [1, 2, 3, 4, 4, 8, 9]


# Key Functions : Both list.sort() and sorted() have a key parameter to specify a function to be called on each list element prior to making comparisons.
# https://docs.python.org/3/howto/sorting.html#sortinghowto

#sort all (we converted the numbers to str before comparison)
print(sorted(myList2, key= lambda x:str(x), reverse= False))
#result : [1, 2, 3, 4, 4, 8, 9, 'a', 'e', 'f', 'i', 'r', 'u']


students = [('Murat',1),('Ali',2),('Ahmet',3),('Kemal',4),('Taner',5)]
print(sorted(students, key= lambda t:t[0], reverse= True))
#result: [('Taner', 5), ('Murat', 1), ('Kemal', 4), ('Ali', 2), ('Ahmet', 3)]

#=============================== lru_cache (Last Recently Used) =============================
from functools import lru_cache

@lru_cache(maxsize=32)
def sum(n):
    print(n)
    return n + 1

sum(1)
#result : 1      2
sum(1)
#result : 1













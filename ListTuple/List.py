myList1 = [1,1.2,(1,2),'a','b','hello world']
print(myList1)
#result: [1, 1.2, (1, 2), 'a', 'b', 'hello world']

myList1 += [5]
myList1.append((1,2,4))
print(myList1)
#result : [1, 1.2, (1, 2), 'a', 'b', 'hello world', 5, (1, 2, 4)]


myList2= "Python is an easy to learn, powerful programming language."
print(myList2.split())
#result : ['Python', 'is', 'an', 'easy', 'to', 'learn,', 'powerful', 'programming', 'language.']

myList3 = [1,2]

def sum(a, b):
    return a + b

s = sum(*myList3)
print(s)
#result: 3



#if list elements are the same type we can concatanate 
myList4 = []
myList4 = myList2 + " Text 4"
print(myList4)
#result: ["Python is an easy to learn, powerful programming language."," Text 4"]

#=======================List Fuctions============================

len(myList3)
#result : 2


myList5 = [1,2,3]
myList6 = [3,4,5]
set(myList5).intersection(myList6)
#result: 3 


set(myList5).difference(myList6)
#result : 1,2

del myList5[1]
print(myList5)
#result : [1,3]

# you can see more at readme.md file

#======================Copy List===================================

#shallow copy 

myList7 = [1,2,3,4]
myList8 = myList7

print(myList8)
#result: [1,2,3,4]

myList7.append(5)
print(myList8)
#result: [1,2,3,4,5]
#we added a element to myList7 but myList8 also affected from this operation.
#in Python assign operation works as shallow copy.

#deep copy

myList9 = myList7[:]
myList7.append(6)

print(myList9)
#result: [1, 2, 3, 4, 5]

#also we can use the copy module
import copy

myList10 = copy.deepcopy(myList7)
myList7.append(7)
print(myList10)

#result: [1, 2, 3, 4, 5, 6]
















































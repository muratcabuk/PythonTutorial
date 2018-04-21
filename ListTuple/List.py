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

















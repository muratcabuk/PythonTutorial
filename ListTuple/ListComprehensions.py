myList1 = [t for t in range(10)]
print(myList1)
#result : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

myList2 = [t for t in range(0,10,2)]
print(myList2)
#result: [0, 2, 4, 6, 8]

myList3 = [(x, y) for x in [1,2,3] for y in [4,5,6]]

#equivalent
#combs = []
#for x in [1,2,3]:
#    for y in [3,1,4]:
#       combs.append((x, y))

print(myList3)

#result: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


myList4 = [(x, y) for x in [1,2,3] if x%2==0 for y in [4,5,6] if y%2==0]
print(myList4)
#result: [(2, 4), (2, 6)]

myList5= [t for t in [g for g in range(1,20,3)] if t%2==0]
print(myList5)
#result: [4, 10, 16]


myList6 = [1, 2, 3, 4]
myList7 = [2, 3, 4, 5]
myList8 = [a for a in myList6 for b in myList7 if a == b]
print(myList8)
#result: [2, 3, 4]

myList10 = [ [a**2, a**3] for a in [1, 2, 3]]
print(myList10)
#result: [[1, 1], [4, 8], [9, 27]]




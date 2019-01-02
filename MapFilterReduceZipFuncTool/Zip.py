


myList= [1,2,3,4,5]
result = zip(myList[0::2],myList[1::2])
print(list(result))
#result = [(1, 2), (3, 4)]

#examples
numberList = [1, 2, 3]
strList = ['one', 'two', 'three']
print(list(zip(numberList, strList)))

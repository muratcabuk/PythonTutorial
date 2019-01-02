myList1 = [1,2,3,4,5,6]
print(myList1[1:5:2])
#result: [2,4]

print(myList1[5:1:-2])
#result: [6,4]

myString="The core of extensible programming is defining functions. Python allows mandatory and optional arguments, keyword arguments, and even arbitrary argument lists."
print(myString[len(myString):0:-1])
#result: .stsil tnemugra yrartibra neve dna ,stnemugra drowyek ,stnemugra lanoitpo dna yrotadnam swolla nohtyP .snoitcnuf gninifed si gnimmargorp elbisnetxe fo eroc eh

print(myList1[0:-1:3])
#result: [1,4]

print(myList1[0:-1:2])
#result: [1,3,5]

print(myList1[1::2])
#result: [2,4,6]



#------------------Multi dimensional (axial) slicing in Python--------------------

myList2 =  [[1,2,3,4,1],
            [1,2,3,4,2],
            [1,2,3,4,3],
            [1,2,3,4,4],
            [1,2,3,4,5]]

#1.take items from 0 to 5
#2.take items from 0 to 5 with step 2 
print(myList2[0:5:1][0:5:2])
#result: [[1, 2, 3, 4, 1], [1, 2, 3, 4, 3], [1, 2, 3, 4, 5]]




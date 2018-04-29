import MyClass1
import datetime 

MyClass1.MyClass1.getMessage()
#result : 'Hello World'

# we cannot call the method like this.
# because getValues() function 
# MyClass1.MyClass1.getValues()

MyClass1.MyClass1.i
#result: 0
m1 = MyClass1.MyClass1("My Text1 ", 1, datetime.datetime.now, [1,2,3])
m1 = MyClass1.MyClass1("My Text 2", 2, datetime.datetime.now, [1,2,3])
m1 = MyClass1.MyClass1("My Text 3", 3, datetime.datetime.now, [1,2,3])

MyClass1.MyClass1.i
#result: 3

del m1
MyClass1.MyClass1.i

#result: 2


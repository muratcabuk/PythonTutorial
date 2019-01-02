import  MyClass1, MyClass2
import datetime 

MyClass1.MyClass1.getMessage()
#result : 'Hello World'

# we cannot call the method like this.
# because getValues() function 
# MyClass1.MyClass1.getValues()

MyClass1.MyClass1.countInherit
#result: 0

m11 = MyClass1.MyClass1(15, "my text", 3, datetime.datetime.now, [1,2,3])

MyClass1.MyClass1.countInherit
#result: 1

m11.countInherit
#result : 1

MyClass1.MyClass.countSuper
#result : 1 

m12 = MyClass1.MyClass1(15, "my text", 3, datetime.datetime.now, [1,2,3])

m12.countInherit
#result : 2

m12.countSuper
#result : 2

MyClass1.MyClass.countSuper
#result : 2




m21 = MyClass2.MyClass2(15, "my text", 3, datetime.datetime.now, [1,2,3])
m22 = MyClass2.MyClass2(15, "my text", 3, datetime.datetime.now, [1,2,3])

m11.countSuper
#result 4

# because all m11,m12, m21, m22 variables read same object (MyClass.countSuper). they have just diffrerent title for same variable
m22.countSuper
#result 4

MyClass1.MyClass1.countSuper
#result : 4

m22.countInherit
#result : 2

m23 = MyClass2.MyClass2(15, "my text", 3, datetime.datetime.now, [1,2,3])

m22.countInherit
#result : 3
m23.countInherit
#result : 3
# because m21, m22, m23 created from same class (MyClass2) and they read same class variable countInherit

MyClass1.MyClass1.countSuper
#result : 5
MyClass2.MyClass2.countSuper
#result : 5












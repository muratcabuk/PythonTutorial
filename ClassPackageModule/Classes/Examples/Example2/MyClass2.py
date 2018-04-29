from MyClass import MyClass 

class MyClass2(MyClass):

    # class variable
    countInherit = 0
    className = "MyClass2"

    # or we can write super class (MyClass1) variable 
    #     def __init__(self, myage, *args, **kwargs):
    def __init__(self, myage,mytext, myint, mydate, mylist):

        # class variable
        MyClass2.countInherit += 1 

        self.myAge=myage,
        super(MyClass2,self).__init__(mytext, myint, mydate, mylist)

    # instance function 
    def setAge(self, myage):
        self.myAge = myage
    
    # class function
    def sayHello():
        print("Hello Hello Hello from MyClass2")

    #overriding base class
    def getClassName():
        print(MyClass2.className)

    def __del__(self):
        MyClass2.countInherit -= 1
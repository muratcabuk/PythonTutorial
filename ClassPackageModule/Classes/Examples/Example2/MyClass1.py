from MyClass import MyClass 

class MyClass1(MyClass):

    # class variable
    countInherit = 0
    className = "MyClass1"


    # or we can write super class (MyClass) variable 
    #     def __init__(self, myage, *args, **kwargs):
    def __init__(self, myage, mytext, myint, mydate, mylist):

        # class variable
        MyClass1.countInherit += 1 
        
        self.myAge=myage,
        super(MyClass1,self).__init__(mytext, myint, mydate, mylist)

    # instance function 
    def setAge(self, myage):
        self.myAge = myage
    
    # class function
    def sayHello():
        print("Hello Hello Hello From MyClass1")

    def __del__(self):
        MyClass1.countInherit -= 1

    # overriding base class
    def getClassName():
        print(MyClass1.className)
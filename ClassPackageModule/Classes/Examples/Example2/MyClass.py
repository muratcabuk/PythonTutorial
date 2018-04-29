import logging

class MyClass(object):
    myName = "Murat Cabuk"
    countSuper = 0
    className = "MyClass"

    #Like Constructor but its not exactly constructor
    def __init__(self, mytext, myint, mydate, mylist):
        # class variable
        MyClass.countSuper +=1 
        logging.info(MyClass.countSuper)
        print(MyClass.countSuper)
        # instance variable
        self.myText=mytext
        self.myInt = myint
        self.myDate = mydate
        self.myList = mylist
    
    #instance function
    def getValues(self):
        print ("-------------myList:")
        print(self.myList)
        print ("-------------myText:")
        print(self.myText)
        print ("-------------myInt:")
        print(self.myInt)
        print ("-------------myDate:")
        print(self.myDate)
        print ("-------------myName:")
        print(self.myName)

    # class function
    def getMessage():
        print ("Hello World")

    #Destructor
    def __del__(self):
        MyClass.countSuper -=1
    
    def getClassName():
        print(MyClass.className)
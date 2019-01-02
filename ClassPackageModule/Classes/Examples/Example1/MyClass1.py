class MyClass1(object):
    myName = "Murat Cabuk"
    i = 0

    #Like Constructor but its not exactly constructor
    def __init__(self, mytext, myint, mydate, mylist):
        # class variable
        MyClass1.i +=1 

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
        MyClass1.i -=1
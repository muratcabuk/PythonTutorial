# Introduction

### source : https://www.python-course.eu/object_oriented_programming.php
### source : http://python-textbok.readthedocs.io/en/1.0/Object_Oriented_Programming.html
### source : https://pythonspot.com/polymorphism/
### source : https://pythonspot.com/method-overloading/



# __ init __  and __ new __function

__ new __ works first. But usually Python programmer prefer to use __ init __ function

Python doesn't have explicit constructors like C++ or Java, but the __ init __ method in Python is something similar, though it is strictly speaking not a constructor. It behaves in many ways like a constructor, e.g. it is the first code which is executed, when a new instance of a class is created. The name sounds also like a constructor __ init __. But strictly speaking it would be wrong to call it a constructor, because a new instance is already "constructed" by the time the method __ init __ is called. 


# Encapsulation

|Name   |Notation   |Behaviour                                                                      |
|-------|-----------|---------                                                                      |
|name   |Public     |Can be accessed from inside and outside                                        |
|_name  |Protected  |Like a public member, but they shouldn't be directly accessed from outside.    |
|__name |Private    |Can't be seen and accessed from outside                                        |


    class Encapsulation(object):
        def __init__(self, a, b, c):
            self.public = a
            self._protected = b
            self.__private = c


    from encapsulation import Encapsulation
    x = Encapsulation(11,13,17)
    x.public
    #11
    x._protected
    #13
    x._protected = 23
    x._protected
    #23
    x.__private
    #Traceback (most recent call last):
    #File "<stdin>", line 1, in <module>
    #AttributeError: 'Encapsulation' object has no attribute '__private'


# Class and Object 

So far we used object variables (also called instance variables). These variables can have and usually have different values for different objects. E.g. Two accounts have different account numbers for sure and normally the balance is also different. Object variables are owned by each individual object or instance of a class. This means that each object has its own copy of the variable. They are called non-static or dynamic variables or members, because they are created for each instance or object. 

Class variables on the other hand are shared by all objects (instances) of that class. They can be accessed and changed by any object. As there is only one copy of an object variable a change of value of such a variable is reflected in all the other instances as well. 

To give you an example of a static or class variable: A counter, a variable to count the total number of accounts can't be a instance variable. To this purpose we define a counter variable, which we place directly below the class statement. Any time the constructor will be called, this variable will be incremented. If an object of an account is deleted, this counter will be decremented.



    class Account(object):
    counter = 0
    def __init__(self, holder, number, balance,credit_line=1500):
        # class variable
        Account.counter += 1
        # instance variable
        self.__Holder = holder
        self.__Number = number
        self.__Balance = balance
        self.__CreditLine = credit_line
    def __del__(self):
        Account.counter -= 1



    from Account import Account
    Account.counter
    #result: 
    a1 = Account("Homer Simpson", 2893002, 2325.21)
    Account.counter
    #result: 1
    a2 = Account("Fred Flintstone", 2894117, 755.32)
    #result: 2
    del a2
    Account.counter
    #result: 1

# Inheritance

you need to reload modules many times. use reload method in importlib module.

if you need to see what is happining in the code (like) debug, use info method from logging module

see Example2


# Polymorphism

Polymorphism is based on the greek words Poly (many) and morphism (forms).  We will create a structure that can take or use many forms of objects.

## Polymorphism with a function

    class Bear(object):
    def sound(self):
        print "Groarrr"
 
    class Dog(object):
        def sound(self):
            print "Woof woof!"
 
    def makeSound(animalType):
        animalType.sound()
 
 
    bearObj = Bear()
    dogObj = Dog()
 
    makeSound(bearObj)
    makeSound(dogObj)



## Polymorphism with abstract class (most commonly used)

    class Document:
        def __init__(self, name):
            self.name = name

        def show(self):
            raise NotImplementedError("Subclass must implement abstract method")

        class Pdf(Document):
            def show(self):
                return 'Show pdf contents!'

        class Word(Document):
            def show(self):
                return 'Show word contents!'

        documents = [Pdf('Document1'),
            Pdf('Document2'),
            Word('Document3')]

        for document in documents:
            print document.name + ': ' + document.show()
        
        #Document1: Show pdf contents!
        #Document2: Show pdf contents!
        #Document3: Show word contents!

# Method Overloading

Because it is a late binding object-oriented language, without type checking, method overloading does not make any sense in Python. Any routine needs to be able to handle all types you pass it. You can implement overloading in all necessary ways in your own code.

in c#

    public void getUser(String user) {
    } 

    public void getUser(int user) {
    }


in python , we dont have type

    def getUser(user):
        pass


# Decorators

## @classmethod

Sözün özü, sınıfın herhangi bir örneğine bağlı olmayan bir işlem yapan, ama anlamsal olarak da sınıfla ilişkili olduğu için sınıf dışında bırakmak istemediğiniz fonksiyonları birer sınıf metodu olarak tanımlayabilirsiniz. (https://belgeler.yazbel.com/python-istihza/nesne_tabanli_programlama2.html)

__A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.__

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters Class method works with the class since its parameter is always the class itself. The class method can be called both by the class and its object.

Class.classmethod()

Or even

    Class().classmethod()

But no matter what, the class method is always attached to a class with first argument as the class itself cls.

    def classMethod(cls, args...)

Example

    import datetime
    class Person(object):
    myList= []
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age=age
        self.birthday= datetime.datetime.now()
        self.myList.append((fullname, age))

    def addBirthday(self, birthday):
        self.birthday = birthday

    def getPerson(self):
        return ("Name {}, Age {}, Birthday {}".format(self.fullname, self.age, self.birthday))
    
    @classmethod
    def getAllPersons(cls):
        return Person.myList


    jhon = Person("John Jhon", 40)
    jhon.addBirthday(datetime.datetime.now())

    jhon.getPerson()
    #result: 'Name Jhon Jhon, Age 40, Birthday 2018-04-29 17:20:34.107901'

    Person.getAllPersons()
    #result : [('Jhon Jhon', 40)]

    jhon.getAllPersons()
    #result : [('Jhon Jhon', 40)]


### __Create factory method using class method__

Factory methods are those methods which return a class object (like constructor) for different use cases.

It is similar to function overloading in C++. Since, Python doesn't have anything as such, class methods and static methods are used.

    from datetime import date

    # random Person
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def fromBirthYear(cls, name, birthYear):
            return cls(name, date.today().year - birthYear)

        def display(self):
            print(self.name + "'s age is: " + str(self.age))

        person = Person('Adam', 19)
        person.display()

        person1 = Person.fromBirthYear('John',  1985)
        person1.display()

        # output
        #Adam's age is: 19
        #John's age is: 31




## @staticmethod

Static methods, much like class methods, are methods that are bound to a class rather than its object.

They do not require a class instance creation. So, are not dependent on the state of the object.

A static method does not receive an implicit first argument. When function decorated with @staticmethod is called, we don’t pass an instance of the class to it (as we normally do with methods). This means we can put a function inside a class but we can’t access the instance of that class (this is useful when your method does not use the instance).

staticmethods can be used when the code that belongs to a class doesn’t use the object itself at all. Python doesn’t have to instantiate a bound method for each object we instantiate. Bound methods are objects too, and creating them has a cost. Having a static method avoids that. There are very few situations where static-methods are necessary in Python.


Example

    class Foo(object):
        name = "murat cabuk"


        @staticmethod
        def mystaticmethod(x, y, z=None):
            #print ('My Static Method')
            #print(Foo.name)
            return x, y, z
            

        #instance method
        def myinstancemethod(self, x, y, z=None):
            #print("mymethod")
            #print(Foo.name)
            return self.myclassmethod(x, y)

        @classmethod
        def myclassmethod(cls, x, y, z=None):
            #print("My Class Method")
            #print(Foo.name)
            return cls.mystaticmethod(x, y, z=z)

    instance = Foo()

    instance.myinstancemethod('x','y')
    #('x', 'y', None)
    instance.myclassmethod('x','y')
    #('x', 'y', None)
    instance.mystaticmethod('x','y')
    #('x', 'y', None)

    #But the class is not usually intended to call the instance method, though it is expected to call the others:

    # we cannot write this call
    #Foo.myinstancemethod('x','y')
    # error : myinstancemethod() missing 1 required positional argument: 'y'
    Foo.myclassmethod('x','y')
    #('x', 'y', None)
    Foo.mystaticmethod('x','y')
    #('x', 'y', None)


### instance method


An instance method is function that is a function of an instance. The function accepts the instance implicitly as an argument to it, and the instance is used by the function to determine the output of the function.

    'ABC'.lower()
    # abc

### Class Method

Remember, in Python, everything is an object. That means the class is an object, and can be passed as an argument to a function.

A class method is a function that is a function of the class. It accepts the class as an argument to it.

The function implicitly knows its own class, the function uses the class to affects the output of the function, and it creates a new one of that class from the iterable. An OrderedDict demonstrates this when using the same method:

    dict.fromkeys('ABC')
    # {'C': None, 'B': None, 'A': None}

### Static Method

a method that "doesn't know its class" - this is a static method in Python. It is merely attached for convenience to the class object. It could optionally be a separate function in another module, but its call signature would be the same.

A static method is a function of neither the class nor the object.

A built-in example of a static method is str.maketrans from Python 3.


    str.maketrans('abc', 'bca')
    #{97: 98, 98: 99, 99: 97}

Given a couple of arguments, it makes a dictionary that is not a function of its class.

It is convenient because str is always available in the global namespace, so you can easily use it with the translate function:

    'abracadabra'.translate(str.maketrans('abc', 'bca'))
    #'bcrbabdbcrb'



# Decorator



    def firstDecorator(func):
        def innerWrapper():
            print("first decorator before")
            func()
            print("first decorator after")
        return innerWrapper

    def secondDecorator(func):
        def innerWrapper():
            print("second decorator before")
            func()
            print("second decorator after")
        return innerWrapper

    @firstDecorator
    @secondDecorator
    def myresult():
        print("hello function")


    myresult()
    #first decorator before
    #second decorator before
    #hello function
    #second decorator after
    #first decorator after

Example

    def tags(tag_name):
        def tags_decorator(func):
            def func_wrapper(name):
                return "<{0}>{1}</{0}>".format(tag_name, func(name))
            return func_wrapper
        return tags_decorator

    @tags("p")
    def get_text(name):
        return "Hello "+name

    print (get_text("John"))
    # Outputs <p>Hello John</p>






# Property Decorator

Property and getter, setter decorator create a property like in C# property.


    class MyClass(object):

        def __init__(self, myname):
            self.myName=myname

        @property
        def Fullname(self):
            print("getting value")
            return self.myName
        
        @Fullname.setter
        def Fullname(self, myname):
            print("settting value")
            self.myName = myname

        @Fullname.deleter
        def Fullname(self):
            del self.myName


    myClass = MyClass("murat cabuk")

    myClass.Fullname = "Murat Cabuk"

    print(myClass.Fullname)
    # Murat Cabuk



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

# example ---------------------------
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


#example ----------------------------------------------
# Passing arguments to decorators

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





    
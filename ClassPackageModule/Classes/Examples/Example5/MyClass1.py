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

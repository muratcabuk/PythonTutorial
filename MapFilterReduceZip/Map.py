#Lambda


def f (x):
    return x**2

print (f(8))
#result: 64

g = lambda x: x**2
print (g(8))
#result: 64


#function returns a function therefore 
def make_incrementor (n):
    #we created a second function using lambda. this function takes a parameter (x)
    return lambda x: x + n 

f = make_incrementor(2)
print(f(3))
#result: 5

print(make_incrementor(2)(3))
#result: 5


#we created a second function using lambda. this function takes a parameter (x,y)
def make_multiply(a,b):
    return lambda x,y:a*b*x*y

print(make_multiply(1,2)(3,4))
#result: 24



def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(list(result))
#result: [1, 4, 9, 16]s


#same usage above using lambda
numbers = (1, 2, 3, 4)
result = map((lambda n:n*n), numbers)
print(list(result))
#result: [1, 4, 9, 16]s












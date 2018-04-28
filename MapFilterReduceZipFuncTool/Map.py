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


#==================================================
#operator.attrgetter(attr)
#operator.attrgetter(*attrs)
#Return a callable object that fetches attr from its operand. If more than one attribute is requested, returns a tuple of attributes. The attribute names can also contain dots. For example:

#After f = attrgetter('name'), the call f(b) returns b.name.
#After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
#After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).


#operator.itemgetter(item)
#operator.itemgetter(*items)
#Return a callable object that fetches item from its operand using the operand’s __getitem__() method. If multiple items are specified, returns a tuple of lookup values. For example:

#After f = itemgetter(2), the call f(r) returns r[2].
#After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
#=================================================


from operator import itemgetter, attrgetter

people = [('Murat',40,'Black','Turkish'),('Jhon',30,'Blue','British'),('Martin',35,'Brown','American'),('Chakie',33,'Black','Chinese')]

#order by second and forth element
print(sorted(people, key=itemgetter(2,3)))
#result: [('Chakie', 33, 'Black', 'Chinese'), ('Murat', 40, 'Black', 'Turkish'), ('Jhon', 30, 'Blue', 'British'), ('Martin', 35, 'Brown', 'American')]

people2 =[{"Name":"Murat", "Age":40, "EyeColor":"Black", "Nationality" : "Turkish"},
            {"Jhon":"Murat", "Age":30, "EyeColor":"Blue", "Nationality" : "Turkish"},
            {"Martin":"Murat", "Age":35, "EyeColor":"Brown", "Nationality" : "Turkish"},
            {"Chakie":"Murat", "Age":33, "EyeColor":"Black", "Nationality" : "Turkish"}]

#order by eyecolor and natinality
print(sorted(people2, key=itemgetter("EyeColor","Nationality")))
#result: [{'Name': 'Murat', 'Age': 40, 'EyeColor': 'Black', 'Nationality': 'Turkish'}, {'Chakie': 'Murat', 'Age': 33, 'EyeColor': 'Black', 'Nationality': 'Turkish'}, {'Jhon': 'Murat', 'Age': 30, 'EyeColor': 'Blue', 'Nationality': 'Turkish'}, {'Martin': 'Murat', 'Age': 35, 'EyeColor': 'Brown', 'Nationality': 'Turkish'}]




class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))


students = [Student('john', 'A', 15),Student('jane', 'B', 12),Student('dave', 'B', 10)]

#ikisi de ayn ı sonuca varır.
print(sorted(students, key=lambda student: student.age))
print(sorted(students, key=attrgetter('grade', 'age')))













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





    


# List and Tuple

source : https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples

## Differences between list and tuple

### Literal

    someTuple = (1,2)
    someList  = [1,2] 

### Size

    a = tuple(range(1000))
    b = list(range(1000))

    a.__sizeof__() # 8024
    b.__sizeof__() # 9088
Due to the smaller size of a tuple operation, it becomes a bit faster, but not that much to mention about until you have a huge number of elements.

### Permitted operations

    b    = [1,2]   
    b[0] = 3       # [3, 2]

    a    = (1,2)
    a[0] = 3       # Error
That also means that you can't delete an element or sort a tuple. However, you could add new element to both list and tuple with the only difference that you will change id of the tuple by adding element
    a     = (1,2)
    b     = [1,2]  

    id(a)          # 140230916716520
    id(b)          # 748527696

    a   += (3,)    # (1, 2, 3)
    b   += [3]     # [1, 2, 3]

    id(a)          # 140230916878160
    id(b)          # 748527696

### Usage

As a list is mutable, it can't be used as a key in a dictionary, whereas a tuple can be used.

    a    = (1,2)
    b    = [1,2] 
    c = {a: 1}     # OK
    c = {b: 1}     # Error

# * Operator

source: https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean

The single star * unpacks the sequence/collection into positional arguments, so you can do this:

    def sum(a, b):
        return a + b

    values = (1, 2)

    s = sum(*values)

This will unpack the tuple so that it actually executes as:

    s = sum(1, 2)

The double star ** does the same, only using a dictionary and thus named arguments:

    values = { 'a': 1, 'b': 2 }
    s = sum(**values)

You can also combine:

    def sum(a, b, c, d):
        return a + b + c + d

    values1 = (1, 2)
    values2 = { 'c': 10, 'd': 15 }
    s = sum(*values1, **values2)

will execute as: 

    s = sum(1, 2, c=10, d=15)

Also see section 4.7.4 - Unpacking Argument Lists of the Python documentation.

Additionally you can define functions to take *x and **y arguments, this allows a function to accept any number of positional and/or named arguments that aren't specifically named in the declaration.
Example:

    def sum(*values):
        s = 0
        for v in values:
            s = s + v
        return s

    s = sum(1, 2, 3, 4, 5)

or with **:

    def get_a(**values):
        return values['a']

    s = get_a(a=1, b=2)      # returns 1

this can allow you to specify a large number of optional parameters without having to declare them.
And again, you can combine:

    def sum(*values, **options):
        s = 0
        for i in values:
            s = s + i
        if "neg" in options:
            if options["neg"]:
                s = -s
        return s

    s = sum(1, 2, 3, 4, 5)            # returns 15
    s = sum(1, 2, 3, 4, 5, neg=True)  # returns -15
    s = sum(1, 2, 3, 4, 5, neg=False) # returns 15

# Function with Description

source: https://www.tutorialspoint.com/python/python_lists.htm

    cmp(list1, list2) 
    Compares elements of both lists.

    len(list) 
    Gives the total length of the list.

    max(list) 
    Returns item from the list with max value.

    min(list) 
    Returns item from the list with min value.

    list(seq) 
    Converts a tuple into list.


# Python includes following list methods

    list.append(obj) 
    Appends object obj to list

    list.count(obj) 
    Returns count of how many times obj occurs in list

    list.extend(seq) 
    Appends the contents of seq to list

    list.index(obj) 
    Returns the lowest index in list that obj appears

    list.insert(index, obj) 
    Inserts object obj into list at offset index

    list.pop(obj=list[-1]) 
    Removes and returns last object or obj from list

    list.remove(obj) 
    Removes object obj from list

    list.reverse() 
    Reverses objects of list in place

    list.sort([func]) 
    Sorts objects of list, use compare func if given
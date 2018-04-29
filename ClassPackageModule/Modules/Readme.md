# Introduction

### source : https://www.tutorialspoint.com/python/python_modules.htm
### source : https://realpython.com/python-modules-packages/



A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.


## How to Import Modules ?

### The Module Search Path

When the interpreter executes the above import statement, it searches for mod.py in a list of directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed


    import sys
    sys.path

    #result

    #['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
    #'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
    #'C:\\Python36', 'C:\\Python36\\lib\\site-packages']

we can also add new path

    sys.path.append(r'C:\Users\murat')
    sys.path

    #result
    #['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
    #'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
    #'C:\\Python36', 'C:\\Python36\\lib\\site-packages', 'C:\\Users\\murat']

## Import

- import module_name
- from module_name import name(s)
- from module_name import *
- import module_name as alt_name
- from module_name import name as alt_name [,  name  as  alt_name  …]

## The dir() Function

The dir() built-in function returns a sorted list of strings containing the names defined by a module.

The list contains the names of all the modules, variables and functions that are defined in a module.

Example

    import math

    content = dir(math)
    print content

    # result 
    #['__doc__', '__file__', '__name__', 'acos', 'asin', 'atan', 
    #'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 
    #'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
    #'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 
    #'sqrt', 'tan', 'tanh']


Module Example

MyModule.py

    def sum(a,b):
        return a+b

MyModuleCaller.py

    import MyModule

    sum(1,2)
    #result 3

    dir(MyModule)
    #result
    #['__builtins__',
    #'__cached__',
    #'__doc__',
    #'__file__',
    #'__loader__',
    #'__name__',
    #'__package__',
    #'__spec__',
    #'sum']

## __name__ variable

if we call the module directly in python terminal like

    import sys
    sys.path

    __name__
    #result: __main__

but if run the pythıb file as a script like

    python MyModule.py

and if we call __ name __ variable in this module we will get the module name. with this variable we can learn that where our code is working.

first time we import the module (file) python interpereter creates a .pyc file.
the file is interpreted and it is ready to run. when we import again pyc file will be execute. there is no need to compile again.

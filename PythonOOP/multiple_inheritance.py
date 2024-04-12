# Inheritance and Multiple Inheritance
class A:  
    pass
class B(A):
    pass

''' In the above example class A is a parent class and class B is
inheriting from class A by passing A as parameter to class B which allows class B 
to access all the attributes and methods of class A'''

# Multiple Inheritance
# Python allows us the ability to perform multiple inheritance between classes

class A:
    a = 1
class B:
    b = 2
class C(A, B):
    pass
c = C()
print(c.a, c.b)  # outputs -> 1 2

# Multi-level inheritance
class A:
    a = 1
class B(A):
    a = 2
class C(B):
    pass
c = C()
print(c.a) # output -> 2 because C derives from the immediate super class B

# Built-in Functions
'''There are two built-in functions that come in handy when trying to find relationship
between different classes and objects i.e. issubclass() and isinstance()'''

# issubclass() example
print(issubclass(A, B)) # output -> False
print(issubclass(B, A)) # output -> True 

'''Child class is passed as the first argument to avoid confusion. This can be read as 
Is B subclass of A?'''

# isinstance() example
class A:
    pass
class B(A):
    pass
b = B()
print(isinstance(b, B)) # True
print(isinstance(b, A)) # True

# super() function example
'''The super() function is a built-in function that can be called inside the derived class 
and gives access to the methods and variables of the parent classes or sibling classes'''

class Fruit:
    def __init__(self, fruit):
        print("Fruit type: ", fruit)
    
class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet!')
apple = FruitFlavour()


'''If I comment super() function the output is 'Apple is sweet!' '''

'''This happened because when we initialize the child class, we don’t initialize 
the parent class with it. super() function helps us to achieve this and add the 
initialization of base class with the derived class.'''


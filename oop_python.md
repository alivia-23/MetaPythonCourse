# OOP in Python
## Encapsulation
The idea of encapsulation is to have **methods** and **variables** within the bound of a given **unit**. In case of Python, it is called a **Class**. And the members of a class become locally bound to that class.

For example, the Little Lemon company may have different departments such as inventory, marketing and accounts. And you may be required to deal with the data and operations for each of them separately. Classes and objects help in encapsulating and in turn restrict the different functionalities.

Encapsulation is also used for hiding data and its internal representation. The term for this is information hiding.  

> Access modifiers represented by keywords called Public, Private and Protected help in data hiding. 

```python
class Alpha:

def __init__(self):
    self._a = 2.  # Protected member ‘a’
    self.__b = 2.  # Private member ‘b’
```
> Protected members can only be accessed by the class and its subclasses
Private members can only be accessed from within the class Alpha

It should be noted that these private and protected members can still be accessed from outside of the class by using public methods to access them or by a practice known as name mangling. Name mangling is the use of two leading underscores and one trailing underscore, for example:

```python
_class__identifier 
```

> Class is the name of the class and identifier is the data member that I want to access.

## Polymorphism

Polymorphism means something that can have **many forms**.  Remember that everything in Python is inherently an **object**, so when I talk about polymorphism, it can be an **operator, method or any object** of some class.
For example:

```python
string = "poly"
num = 7
sequence = [1, 2, 3]
new_str = string * 3
new_num = num * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)
```
The output is:
```Python
polypolypoly 21 [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## Inheritance

```Python
class Parent:
    Members of the parent class

class Child(Parent):
    Inherited members from parent class
    Additional members of the child class
```
As the structure of inheritance gets more complicated, Python adheres to something called the **Method Resolution Order (MRO)** that determines the flow of execution. MRO is a set of rules, or an algorithm, that Python uses to implement monotonicity, which refers to the order or sequence in which the interpreter will look for the variables and functions to implement. This also helps in determining the scope of the different members of the given class.

## Abstarction
Abstraction can be seen both as a means for **hiding important information** as well as **unnecessary information** in a block of code. The core of abstraction in Python is the implementation of something called **abstract classes and methods**, which can be implemented by inheriting from something called the **abc module**. "abc" here stands for **abstract base class**. It is first imported and then used as a parent class for some class that becomes an abstract class. 

```Python
from abc import ABC,   
class ClassName(ABC):
    pass
```


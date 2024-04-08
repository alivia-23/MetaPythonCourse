# OOP in Python
## Encapsulation
The idea of encapsulation is to have methods and variables within the bound of a given unit. In case of Python, it is called a Class. And the members of a class become locally bound to that class.

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

> ```python
_class__identifier 
```

Class is the name of the class and identifier is the data member that I want to access.

## Polymorphism


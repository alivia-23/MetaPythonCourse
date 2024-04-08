# Instantiation in python involves 3 key steps
# 1. Class definition
# 2. Creating a new instance
# 3. Initializing the new instance

# Classes mainly perform 2 kinds of operation
# Attribute reference and instantiation

class MyClass:
    a = 5
    print("Hello")

    def hello(self):
        print("Hello World!")

myc = MyClass()
print(myc.a) # output 5 , attribute referrence
print(MyClass.a) # output 5 , class referrence
print(myc.hello())
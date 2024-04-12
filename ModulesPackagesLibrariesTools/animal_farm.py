def d():
    # local value of animal 
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function: " +animal)

    print("Before calling function: " +animal)
    e()
    print("After nested function: " +animal)

# Global variable
animal = "camel"
d()
print("Global animal: " + animal)
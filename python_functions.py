def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print('Total Tax: ',calculate_tax(175.00, 15))

print('Total Tax: ', calculate_tax(164.33, 22))

#Global function and function scoping
my_global = 10

def fn1():
    enclosed_v = 5

    def fn2():
        local_v = 5
        print('Access to global', my_global)
        print("Access to enclosed", enclosed_v)
    fn2()
fn1()

#Local scope
def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2)) # output -> 7

# Accessing variable outside of the function:
print(total) # output -> NameError: name 'total' is not defined

#Enclosing scope
def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    print(double)

    return total

# Global Scope
special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total
coffees = ['Espresso', 'Latte', 'Cappucino', 'Macchiato', 'Americano', 'Decaf']
def reverse(str):
    return str[::-1]
reversed_coffees = map(reverse, coffees)
for x in reversed_coffees:
    print(x)

# A Pure function does not change or have any effect on data, variable, list or set beyond its own scope
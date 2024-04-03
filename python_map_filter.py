# filter this for a specific set of elements
menu = ["espresso", "mocha", "latte", "cappucino", "cortado", "americano"]
# filter all coffees that starts with the letter 'c'
def find_coffee(coffee):
    if (coffee[0] == 'c'):
        return coffee
    
# Method 1 : Using Map() function
map_coffee = map(find_coffee, menu)
print(map_coffee)

for x in map_coffee:
    print(x)

# Method 2 : Filter function
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)


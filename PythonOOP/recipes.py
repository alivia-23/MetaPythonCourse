class Recipe:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def content(self):
        print("The " +  self.dish + " has " + str(self.items) + " and takes " + \
              str(self.time) + " min to prepare.")
        
pizza = Recipe("Pizza", ["cheeze", "bread", "tomato", "ketchup"], 45)
pasta = Recipe("Pasta", ["penne", "cheeze", "ketchup"], 55)

print(pizza.items)
print(pasta.items)

print(pizza.content())
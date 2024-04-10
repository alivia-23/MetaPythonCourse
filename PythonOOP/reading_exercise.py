# Define class MyFirstClass
class MyFirstClass:
    print("Who wrote this?")

    # Define string variable called index
    index = "Author-Book"
    
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book

        # variable + “ wrote the book: ” + variable
        print(self.philosopher + " wrote the book: " + self.book)

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Plato", "Republic")
whodunnit.hand_list("Sun Tzu", "The Art of War")

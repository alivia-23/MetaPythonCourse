# Note : Tuples are immutable data structure
my_tuple = (1, 2, 2, 'strings', 4.5, True)
print(my_tuple[1]) # returns strings

# Determine type of the tuple
print(type(my_tuple)) # return <class 'tuple'>
print(type(my_tuple[1])) # return <class 'str'>

# it can count the number of occurences of certain element in the tuple
print(my_tuple.count('strings'))
print(my_tuple.count(2))

print("******************")
for x in my_tuple:
    print(x)
print("******************")

# Tuples are immutable for example

my_tuple[2] = 3
print(my_tuple) # this will throw an error i.e. /TypeError: 'tuple' object does not support item assignment/


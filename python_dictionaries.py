# Dictionaries are mutable
sample_dict = {1: 'Coffee', 2: 'Tea', 3:'Juice', 'Name': 'John'}
# access data from dictionary by using the keys
print(sample_dict[2]) # output -> Tea
# <class 'dict'>
print(type(sample_dict))
# Update data in dictionary
sample_dict[2] = 'Mint Tea'
print(sample_dict) # output -> 1: 'Coffee', 2: 'Mint Tea', 3: 'Juice', 'Name': 'John'}
# Delete data from dictionary
del sample_dict[3]
print(sample_dict) # output -> {1: 'Coffee', 2: 'Mint Tea', 'Name': 'John'}

# Dictionaries doesn't allow duplicate keys

# Iterate over dictionaries
for x in sample_dict:
    print(x) # It will print out the keys i.e. 1, 2, Name

# To get both the key and value
for key, value in sample_dict.items():
    print(str(key) + " : " + value) # we should be mindful of type of our keys since we have int and string both as keys



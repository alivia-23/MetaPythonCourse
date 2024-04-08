# Generator comprehensions are also very similar to lists with the variation of using curved brackets instead 
# of square brackets. They are also more memory efficient as compared to list comprehensions. 
# For example:

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")



# Note:
# List comprehensions also provide direct return of a list as compared to map() function that returns a 
# map object. It is mainly the clarity that has made list comprehensions popular, but map() functions are 
# still arguably a better choice when it comes to the use of larger sequences.
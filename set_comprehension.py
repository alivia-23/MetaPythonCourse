# The set comprehension deals with the set data type and it's very similar to list comprehension. 
# The only key difference is the use of curly brackets for sets instead of square brackets as in lists.
# For example:
list_num = [12, 14, 16]
set_a = {x for x in range(10, 20) if x not in list_num}
print(set_a)
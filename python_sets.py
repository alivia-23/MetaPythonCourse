set_a = {1, 2, 3, 4, 5, 5}
set_a.add(6)
print(set_a) # output -> {1, 2, 3, 4, 5, 6} it won't print the duplicate value
set_a.remove(2)
print(set_a)  # output -> {1, 3, 4, 5, 6}

set_b = {4, 5, 6, 7, 8}
print(set_a.union(set_b)) # output -> {1, 3, 4, 5, 6, 7, 8} 
# in union method it'll remove the duplicate values from both the sets and give a single set by combining both
# alternate way of combining two sets
print(set_a | set_b) # output -> {1, 3, 4, 5, 6, 7, 8} same as union

# find common elements of set_a and set_b
print(set_a.intersection(set_b)) # output -> {4, 5, 6}
# intersection can also be represented as
print(set_a & set_b) # output -> {4, 5, 6}

# find the difference of set_a and set_b i.e. the elements that are only in set_a and not in set_b
print(set_a.difference(set_b)) # output -> {1, 3}
# can also be represented as 
print(set_a - set_b) # output -> {1, 3}

# Symmetrical Difference i.e. all elements that are present in a and b but not in both
print(set_a.symmetric_difference(set_b)) # output -> {1, 3, 7, 8}
# can also be represented as
print(set_a ^ set_b) # output -> {1, 3, 7, 8}

# a set is unordered lists of item i.e. if we want to access elements by specifying index we get error
print(set_a[0]) # output -> TypeError: 'set' object is not subscriptable
# Not a pure function as add-to_list function modifies the outer list
my_list = [1, 2, 3]
def add_to_list(item):
    return my_list.append(item)
add_to_list(4)
print(my_list) # [1, 2, 3, 4]

# Pure function implementation
my_list1 = [1, 2, 3]
def add_to_list1(lst, item):
    new_list = lst.copy()
    new_list.append(4)
    return new_list

new_list = add_to_list1(my_list1, 4)
print(my_list1) # [1, 2, 3]
print(new_list) # [1, 2, 3, 4]

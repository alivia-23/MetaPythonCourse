list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C']
list3 = ['hello', 1, True, 40.22]
list4 = [1, [2, 3, 4], 5, 6]

# print the entire list
print(*list1)

# print with a comma and in a box trsucture like the input
print(list1, sep=" ")

# Insering element in lists methods
# list1.insert(len(list1), 6)
# list1.append(6)
list1.extend([6, 7, 8, 9])
print(list1, sep=" ")

# Deleting elements from the lists
list1.pop(4) # the item with index 4 will be deleted

# another method of deleting
del list1[2] # delete element at index 2
print(list1, sep=" ")

# Iterate over lists

for i in list1:
    print('Value', i)

# Syntax for List comprehension
# [<expression> for x in <sequence> if <condition>]

data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: Updating the same list
data = [ x + 3 for x in data]
print('Updating the list: ', data)

# Ex2: Creating a different list with updated values
new_data = [ x * 3 for x in data]
print('Creating a different list with the updated list: ', new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
print('Numbers divisible by four: ',fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
print('Numbers divisible by four minus one: ', fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print('Divisible by Nines from 0 to 100: ', nines)
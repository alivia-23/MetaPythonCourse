# args as parameter allows us to pass any number of arguements in a function
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4, 5, 6, 7, 8, 9)) # output -> 39
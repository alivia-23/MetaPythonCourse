def divide_by(a, b):
    return a / b
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero!")
    print(e.__class__)
except Exception as e:
    print(e, "Something went wrong!")
#print(e.__class__)
# print(divide_by(40, 4)) # output -> 10.0
# print(divide_by(40, 0)) # output -> ZeroDivisionError: division by zero
# Question 1:
def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)

# Question 4:
numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)
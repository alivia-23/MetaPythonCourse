# with kwargs you can pass any amount of keyword arguments
def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99)) # output -> 10.53
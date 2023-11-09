def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print('Total Tax: ',calculate_tax(175.00, 15))

print('Total Tax: ', calculate_tax(164.33, 22))

#Global function and function scoping
my_global = 10

def fn1():
    enclosed_v = 5

    def fn2():
        local_v = 5
        print('Access to global', my_global)
        print("Access to enclosed", enclosed_v)
    fn2()
fn1()

# String reversal using recursion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        first = str[0]
        rem = str[1:]
        return string_reverse(rem) + first
    
str = "reversal"
reverse = string_reverse(str)
print(reverse)
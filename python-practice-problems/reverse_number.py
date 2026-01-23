# using string converstion method
def reverse_digit(n):
    result = ''
    
    s = str(n)
    for i in reversed(s):
        result += i
    return int(result)

print(reverse_digit(567))
# using math remainder method
def reverse_digit_using_remainder(n):
    result = 0
    while n!= 0:
        result = result * 10 + (n % 10)
        n = n // 10
    return result
print(reverse_digit_using_remainder(567))

# using recursion method 
def reverse_digit_using_recursion(n, reverse_num):
    if n == 0:
        return reverse_num
    reverse_num = reverse_num * 10 +(n % 10)
    return reverse_digit_using_recursion(n // 10, reverse_num)
    
print(reverse_digit_using_recursion(567,0))
    

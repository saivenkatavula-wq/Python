# using maths
def sum_of_digits(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum

print(sum_of_digits(678))

# using recursion
def sum_of_digits_recursion(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursion(n = n //10)
print(sum_of_digits_recursion(678))

# using string conversion
def sum_of_digits_string_converstion(n):
    sum = 0
    s = str(n)
    for i in s:
        sum += int(i)
    return sum
print(sum_of_digits_string_converstion(678))

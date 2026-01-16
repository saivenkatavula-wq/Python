def n_natural_numbers(n):
    if n == 1:
        return 1
    return n + n_natural_numbers(n-1)
x = n_natural_numbers(5)
print(x)
        

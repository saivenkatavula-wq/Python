# loop based solution
def close_to_n_divisible_by_m(n, m):
    closest = 0
    min_difference = float('inf')
    for i in range(n-abs(m),n+abs(m)+1):
        if i % m == 0:
            difference = abs(n-i)
            if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
                closest = i
                min_difference = difference
    return closest
print(close_to_n_divisible_by_m(-15,6))

# math based solution
def close_to_n_divsible_by_m(n,m):
    m = abs(m)
    lower = n - (n%m)
    higher = lower + m
    
    if abs(n-lower) < abs(n-higher):
        return lower
    elif abs(n-lower) > abs(n-higher):
        return higher
    else:
        if abs(lower) > abs(higher):
            return lower
        else:
            return higher

 
print(close_to_n_divsible_by_m(13,-4))

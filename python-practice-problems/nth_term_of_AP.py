# using loop method
import itertools
def nth_term_of_AP(a,b,n):
    step = b - a
    return next(itertools.islice(itertools.count(a,step),n - 1, n))

print(nth_term_of_AP(2,3,4))
# using formula
import itertools
def nth_term_of_AP(a,b,n):
    return (a + (n-1) * (b - a))

print(nth_term_of_AP(2,3,4))

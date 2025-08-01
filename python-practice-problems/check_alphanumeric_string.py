# Approach 1 - using two build-in's python methods
s = "hello123"

l = any(c.isalpha() for c in s)

k = any(c.isdigit() for c in s)

if l and k:
    print("TRUE")
else:
    print("FALSE")

# Approach 2 - only one build-in python methods

if s.isalnum():
    print("TRUE")
else:
    print("FALSE")

# Approach 3 - using regular expressions

import re

l = bool(re.search(r'[a-zA-Z]', s))
n = bool(re.search(r'\d', s))

if l and n:
    print("TRUE")
else:
    print("FALSE")

# Approach 4 -  using no build-in's or any modules

def is_alphanumeric(s):
    has_alpha = False
    has_digit = False
# even here i am not using any build-in but under the hood the python is still converting
# the given string into the ascii value and compare it with the ascii value of the character
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_alpha = True
        elif '0' <= char <= '9':
            has_digit = True

    if has_alpha and has_digit:
        return True
    else:
        return False


is_alphanumeric(s)




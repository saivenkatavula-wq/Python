def reverseString(n):
    stack = list(n)
    final_string = "".join(stack.pop() for _ in range(len(stack)))
    print(final_string)

n = input("enter the string: ")
reverseString(n)

def pyramdi(n):
    if n > 0:
        pyramdi(n - 1)
        print("*" * n)
n = int(input("Enter a number: "))
pyramdi(n)

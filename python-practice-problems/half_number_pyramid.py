def numpy(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end="")
            num += 1
        print()
        num = 1

n = int(input("Enter a number: "))
numpy(n)

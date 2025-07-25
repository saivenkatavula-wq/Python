def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()


n = int(input("Enter a number: "))
half_pyramid(n)

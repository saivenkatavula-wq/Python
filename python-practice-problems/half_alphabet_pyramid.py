def alphpyramid(n):
    alph = 65
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(alph), end="")
        alph += 1
        print()


alphpyramid(5)

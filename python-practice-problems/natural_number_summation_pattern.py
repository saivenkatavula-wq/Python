n = int(input("Enter a number: "))
for i in range(1, n + 1):
    a = []
    total = 0
    for j in range(1, i + 1):
        print(j, sep=' ', end=' ')
        total += j
        if j < i:
            print("+ ",sep=" ", end='')
        a.append(j)
    print("= ", total)

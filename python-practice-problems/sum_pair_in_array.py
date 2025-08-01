def findPair(a, z):
    pair = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] + a[j] == z:
                pair.append((a[i], a[j]))
    return print(pair)

findPair([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)

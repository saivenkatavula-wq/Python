def pos(n):
    if n == 0:
        print("already Zero")
    else:
        while(n > 0):
            n -= 1
            print(n, end=" ")
        
def neg(n):
    if n == 0:
        print("already Zero")
    else:
        while (n <= 0):
            print(n, end=" ")
            n += 1

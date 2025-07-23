def print_spaces(spaces):
    if spaces > 0:
        print(" ", end="")
        print_spaces(spaces - 1)


def print_stars(stars):
    if stars > 0:
        print("*", end="")
        print_stars(stars - 1)


def print_pyramid(n, current_row=1):
    if current_row > n:
        return
    spaces = n - current_row

    stars = 2 * current_row - 1

    print_spaces(spaces)

    print_stars(stars)

    print()

    print_pyramid(n, current_row + 1)


n = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(n)

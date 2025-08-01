s = "aeiouAEIOU"
inp = input("Enter a string: ")


def only_vowels(inp):
    has_consonants = False
    for i in inp:
        if i not in s:
            has_consonants = True

    if not has_consonants:
        print("String contains only vowels.")
    else:
        print("String not only contain vowels.")

only_vowels(inp)

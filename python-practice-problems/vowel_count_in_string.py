s = "hello"
vowels = 'aeiouAEIOU'

def count_vowels(s):
    vowel_count = 0
    for i in s:
        if i in vowels:
            vowel_count += 1
    return print(vowel_count)

count_vowels(s)

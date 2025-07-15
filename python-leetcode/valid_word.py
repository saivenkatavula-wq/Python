class Solution(object):
    def isalphanum(self, word):
        for char in word:
            if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
                return False
        return True

    def has_vowel_and_consonant(self, word):
        vowels = "aeiouAEIOU"
        has_vowel = False
        has_consonant = False
        for char in word:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel, has_consonant

    def isValid(self, word):
        if len(word) >= 3 and self.isalphanum(word):
            has_vowel, has_consonant = self.has_vowel_and_consonant(word)
            if has_vowel and has_consonant:
                return True
        return False

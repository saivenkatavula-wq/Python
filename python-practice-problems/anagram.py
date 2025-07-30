class Solution:
    def areAnagrams(self, s1, s2):
        char_dict = {}
        if len(s1) != len(s2):
            return False
        for ch in s1:
            if ch in char_dict:
               char_dict[ch] += 1
            else:
                char_dict[ch] = 1
        for ch in s2:
            if ch in char_dict:
                char_dict[ch] -= 1
        for count in char_dict.values():
            if count != 0:
                return False

        return True
       

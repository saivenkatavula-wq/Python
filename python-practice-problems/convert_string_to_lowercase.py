class Solution:
    def toLower (self , s : str)-> str :
        result = ''
        for i in s:
            if 65 <= ord(i) <= 90:
                result += chr(ord(i) + 32)
            else:
                result += i
        return result

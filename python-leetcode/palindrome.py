class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        reversed_str = s[::-1]
        if s == reversed_str:
            return True
        else:
            return False

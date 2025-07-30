class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_str = s[::-1]
        if reverse_str == s:
            return True
        else:
            return False

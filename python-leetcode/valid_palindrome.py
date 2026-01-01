class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        cleaned_s = re.sub('[^a-z0-9]', '', s)
        return cleaned_s == cleaned_s[::-1]


        

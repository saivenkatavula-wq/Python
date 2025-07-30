class Solution:
    def reverseWords(self, s):
        # using split for normalizing the string
        words = []
        parts = s.split('.')
        for part in parts:
            if part != '':
                words.append(part)
        # using stack for the reverse the words
        stack = []
        for word in words:
            stack.append(word)
            
        reversed_words = []
        while stack:
            reversed_words.append(stack.pop())
        # joining the words 
        return '.'.join(reversed_words)
        
        
            
        

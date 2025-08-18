#Method 1
class Solution(object):
    def longestValidParentheses(self, s):
        left_bracket = 0
        right_bracket = 0
        best = 0
        for i in s:
            if i == '(':
                left_bracket += 1
            else:
                right_bracket += 1
            if left_bracket == right_bracket:
                best = max(best, 2 * right_bracket)
            else:
                if right_bracket > left_bracket:
                    right_bracket = 0
                    left_bracket = 0

        right_bracket = 0
        left_bracket = 0
        for i in reversed(s):
            if i == '(':
                left_bracket += 1
            else:
                right_bracket += 1
            if left_bracket == right_bracket:
                best = max(best, 2 * right_bracket)
            else:
                if left_bracket > right_bracket:
                    right_bracket = 0
                    left_bracket = 0

        return best
# using stack
class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        best = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])
        return best



            

        




            

        

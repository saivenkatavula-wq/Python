class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            elif ch in brackets:
                if not stack or stack.pop() != brackets[ch]:
                    return False
            else:
                return False

        return not stack

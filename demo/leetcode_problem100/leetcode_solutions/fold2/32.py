class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(': # opening parenthesis
                stack.append(i)
            else: # closing parenthesis
                stack.pop()
                if len(stack) == 0: # no more valid substring
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)
        return max_length
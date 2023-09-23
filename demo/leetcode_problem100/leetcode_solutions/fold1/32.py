class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':  # If opening parenthesis
                stack.append(i)  # Push its index onto the stack
            else:  # If closing parenthesis
                stack.pop()  # Pop the top element from stack
                if len(stack) == 0:  # If stack is empty
                    stack.append(i)  # Push current index onto stack
                else:  # If stack is not empty
                    max_length = max(max_length, i - stack[-1])  # Update max length
        return max_length
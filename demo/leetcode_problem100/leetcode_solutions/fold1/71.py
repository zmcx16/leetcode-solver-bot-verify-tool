class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        elements = path.split('/')
        for element in elements:
            if element == '..':
                if stack:
                    stack.pop()
            elif element == '.' or element == '':
                continue
            else:
                stack.append(element)
        return '/' + '/'.join(stack)
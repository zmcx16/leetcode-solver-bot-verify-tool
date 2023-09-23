class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        for directory in directories:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        return '/' + '/'.join(stack)
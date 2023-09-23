def longestCommonPrefix(self, strs):
    if not strs:
        return ''
    prefix = ''
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return prefix
        prefix += char
    return prefix
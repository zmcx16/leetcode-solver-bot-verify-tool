class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        if words:
            return len(words[-1])
        else:
            return 0
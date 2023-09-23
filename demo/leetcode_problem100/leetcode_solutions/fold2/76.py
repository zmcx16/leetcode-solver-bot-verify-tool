class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        left = 0
        right = 0
        window_freq = {}
        formed = 0
        ans = float('inf'), None, None
        while right < len(s):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed += 1
            while left <= right and formed == len(t_freq):
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_freq[char] -= 1
                if char in t_freq and window_freq[char] < t_freq[char]:
                    formed -= 1
                left += 1
            right += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
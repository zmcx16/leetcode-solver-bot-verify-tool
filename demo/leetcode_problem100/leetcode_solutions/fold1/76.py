class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        required_chars = len(freq_t)
        left = right = 0
        min_window_size = float('inf')
        start = end = 0

        while right < len(s):
            if s[right] in freq_t:
                freq_t[s[right]] -= 1
                if freq_t[s[right]] == 0:
                    required_chars -= 1

            while required_chars == 0:
                if right - left + 1 < min_window_size:
                    min_window_size = right - left + 1
                    start = left
                    end = right

                if s[left] in freq_t:
                    freq_t[s[left]] += 1
                    if freq_t[s[left]] > 0:
                        required_chars += 1

                left += 1

            right += 1

        if min_window_size == float('inf'):
            return ''
        else:
            return s[start:end+1]
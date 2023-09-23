class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for i in range(len(s)):
            curr_value = roman_values[s[i]]
            if curr_value > prev_value:
                total -= prev_value
            else:
                total += prev_value
            prev_value = curr_value
        total += prev_value
        return total
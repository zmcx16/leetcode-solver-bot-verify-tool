class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        reverse_str = str(x)[::-1]
        reverse_int = int(reverse_str) * sign
        if reverse_int < -2**31 or reverse_int > 2**31 - 1:
            return 0
        return reverse_int
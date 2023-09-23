class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            return float('inf')
        is_negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        if is_negative:
            quotient = -quotient
        if quotient > 2**31 - 1:
            return 2**31 - 1
        if quotient < -2**31:
            return -2**31
        return quotient
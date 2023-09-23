class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return '1.00000'
        elif n > 0:
            result = 1
            for _ in range(n):
                result *= x
            return str(result)
        else:
            result = 1
            for _ in range(-n):
                result *= x
            return str(1 / result)
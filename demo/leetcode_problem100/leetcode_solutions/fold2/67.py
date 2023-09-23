class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_decimal = int(a, 2) + int(b, 2)
        sum_binary = bin(sum_decimal)[2:]
        return sum_binary
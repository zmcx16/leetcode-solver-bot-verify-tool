class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_decimal = int(a, 2) + int(b, 2)
        sum_binary = bin(sum_decimal)
        return sum_binary[2:]

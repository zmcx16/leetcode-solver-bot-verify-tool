class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        for i in range(n2 - 1, -1, -1):
            carry = 0
            for j in range(n1 - 1, -1, -1):
                product = int(num2[i]) * int(num1[j]) + carry
                carry = (result[i + j + 1] + product) // 10
                result[i + j + 1] = (result[i + j + 1] + product) % 10
            result[i] = carry
        if result[0] == 0:
            result = result[1:]
        return ''.join(map(str, result))
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        product = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                curr_product = int(num1[i]) * int(num2[j])
                carry = curr_product // 10
                curr_product %= 10
                product[i + j + 1] += curr_product
                if product[i + j + 1] >= 10:
                    carry += product[i + j + 1] // 10
                    product[i + j + 1] %= 10
                product[i + j] += carry
        if product[0] == 0:
            product = product[1:]
        return ''.join(map(str, product))
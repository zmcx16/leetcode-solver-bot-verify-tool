class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev_gray_code = self.grayCode(n-1)
        return prev_gray_code + [x + (1 << (n-1)) for x in reversed(prev_gray_code)]

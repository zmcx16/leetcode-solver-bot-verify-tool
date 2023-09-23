class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack('', 0, 0, n, result)
        return result

    def backtrack(self, current: str, open_paren: int, close_paren: int, max_paren: int, result: List[str]) -> None:
        if len(current) == max_paren * 2:
            result.append(current)
            return

        if open_paren < max_paren:
            self.backtrack(current + '(', open_paren + 1, close_paren, max_paren, result)

        if close_paren < open_paren:
            self.backtrack(current + ')', open_paren, close_paren + 1, max_paren, result)

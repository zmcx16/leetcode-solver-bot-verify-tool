class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(output, open_count, close_count, max_count):
            if len(output) == 2 * max_count:
                combinations.append(output)
                return
            if open_count < max_count:
                backtrack(output + '(', open_count + 1, close_count, max_count)
            if close_count < open_count:
                backtrack(output + ')', open_count, close_count + 1, max_count)
        combinations = []
        backtrack('', 0, 0, n)
        return combinations
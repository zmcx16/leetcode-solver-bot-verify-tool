class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def generate_combinations(current_combination, remaining_digits):
            if len(remaining_digits) == 0:
                return [current_combination]
            digit = remaining_digits[0]
            letters = digit_to_letters[digit]
            combinations = []
            for letter in letters:
                combinations.extend(generate_combinations(current_combination + letter, remaining_digits[1:]))
            return combinations
        return generate_combinations('', digits)
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def backtrack(nums, curr): # helper function to generate permutations
            nonlocal k
            if len(curr) == n: # base case: current permutation is complete
                k -= 1
                if k == 0: # if kth permutation is found, return it
                    return ''.join(curr)
                return
            for num in nums: # try adding each number to the current permutation
                if num not in curr: # skip numbers that have already been used
                    curr.append(num)
                    result = backtrack(nums, curr) # recursively generate next permutation
                    if result: # if kth permutation is found, return it
                        return result
                    curr.pop() # backtrack by removing the last added number from the current permutation
        nums = [str(i) for i in range(1, n+1)] # convert numbers to strings
        return backtrack(nums, [])
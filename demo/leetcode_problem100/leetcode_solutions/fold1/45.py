class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps = 1
        current_reach = nums[0]
        max_reach = nums[0]
        for i in range(1, len(nums)):
            if i > current_reach:
                jumps += 1
                current_reach = max_reach
            max_reach = max(max_reach, i + nums[i])
        return jumps
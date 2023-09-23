class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        jumps = 1
        current_step_boundary = nums[0]
        next_step_boundary = nums[0]
        for i in range(1, n):
            if i > current_step_boundary:
                jumps += 1
                current_step_boundary = next_step_boundary
            next_step_boundary = max(next_step_boundary, i + nums[i])
        return jumps
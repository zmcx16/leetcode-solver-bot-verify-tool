class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		result = [[]]
		for num in nums:
			result += [subset + [num] for subset in result if subset and subset[-1] != num]
		return json.dumps(result)
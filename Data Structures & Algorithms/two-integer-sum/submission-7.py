class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                k = num1+nums[j]
                if k == target:
                    return [i,j]
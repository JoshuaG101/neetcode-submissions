class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums)
        return (sortedNums[-k])
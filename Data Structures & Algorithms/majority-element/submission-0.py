class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mostElem = {}

        for val in range(len(nums)):
            if nums[val] not in mostElem:
                mostElem[nums[val]] = 1
            else:
                mostElem[nums[val]] += 1
        return max(mostElem, key=mostElem.get)            


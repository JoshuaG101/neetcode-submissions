class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets,res = [],[] 
        
        def dfs(i):
            if i == len(nums):
                res.append(subsets.copy())
                return

            dfs(i+1)
            subsets.append(nums[i])

            dfs(i +1)
            subsets.pop()
        dfs(0)
        return res
            

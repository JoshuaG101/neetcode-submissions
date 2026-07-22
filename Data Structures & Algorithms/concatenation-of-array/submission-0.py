class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i,n in enumerate((nums)*2):
            ans.append(n)
        return ans
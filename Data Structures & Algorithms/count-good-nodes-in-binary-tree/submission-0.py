# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        1. is the whole tree to keep track
        2. root node is alway true
        3. not in order
        4. always have to check the whole tree o(n)
        5. prob use a seen set to keep track 

        """
        def dfs(root, maxX):
            if not root:
                return 0
            res = 1 if root.val >= maxX else 0
            maxX = max(maxX, root.val)
            res += dfs(root.left, maxX)
            res += dfs(root.right, maxX)
            return res

        return dfs(root, root.val)
        
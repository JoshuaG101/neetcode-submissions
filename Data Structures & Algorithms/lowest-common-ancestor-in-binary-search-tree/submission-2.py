# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # If both nodes are smaller, move left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both nodes are larger, move right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # We found the split point!
            else:
                return root
        
        return None

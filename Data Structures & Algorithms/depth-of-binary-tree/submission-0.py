# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        

        def dfs(node, val):
            if not node:
                return val
            

            left = dfs(node.left, val+1)
            right = dfs(node.right, val+1)
        
            return max(left, right)
    
        return dfs(root, 0)
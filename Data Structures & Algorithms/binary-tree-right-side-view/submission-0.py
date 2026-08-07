# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []


        while q:

            level_res = [] 
            right_mode = None

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    right_mode = node.val
                    q.append(node.left)
                    q.append(node.right)
            
            if right_mode:
                res.append(right_mode)
        
        return res
                    
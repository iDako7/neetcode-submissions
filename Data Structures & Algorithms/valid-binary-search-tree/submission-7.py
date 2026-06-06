# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        res = True
        def dfs(node, low, high):
            if not node: return False

            # validate root first
            if not root.val between the val of left and right:
                res = False
                return
            # then left and right
            left = dfs(node.left, low, root.val)
            right = dfs(node.right, root.val, hight)

        return res
        """

        res = True

        def dfs(node, low, high):
            nonlocal res

            if not node:
                return
            
            if not(low < node.val < high):
                res = False
                return
            
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
        
        dfs(root, float('-inf'),float('inf'))

        
        return res

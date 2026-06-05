# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs to check height
            # left: is it balanced and its height
            # height: is it balanced and its height
            # if not balanced: return false 
            # if this root is balance: not, return false
            # return 1 + max(left, right)
        
        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            left = dfs(node.left)
            if balanced is False:
                return 0
            
            right = dfs(node.right)
            if balanced is False:
                return 0
            
            # check whether current node is balanced
            if abs(left - right) > 1:
                balanced = False

            return 1 + max(left, right)  
        
        dfs(root)
        return balanced


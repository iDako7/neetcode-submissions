# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        root is the ancestor of all nodes
        if both node is in same side, then there is a lowwer ancestor
        -- node.val is between them, then this is LCA
        """
        res = root

        def dfs(node):
            nonlocal res

            # edge case
            if not node:
                return
            
            
            # check whether in the range
            # if yes, then found
            # if both less, then go left; otherwise go right
            if p.val < node.val and q.val < node.val:
                dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                dfs(node.right)
            else:
                # 3 < 5 < 8
                # 3 = 3 < 4
                res = node
                return
            
        dfs(root)
        return res

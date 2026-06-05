# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # def search
            # if p and q < root:
                # go left
            # if p and q > root:
                # go right
            # else, root in the middle
                # return root
        
        res = root

        def search(node):
            nonlocal res
            if not node:
                return
            
            val = node.val

            if p.val > val and  q.val > val:
                search(node.right)
            
            
            elif q.val < val and p.val < val:
                search(node.left)
            else:
                res = node
        
        search(root)
        return res
        

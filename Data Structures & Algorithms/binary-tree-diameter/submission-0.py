# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # largest diameter
        res = 0 

        def height(root):
            nonlocal res

            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            # diameter at this node
            res = max(left_height + right_height, res)

            # the height which parent node could build on
            return 1 + max(left_height, right_height)
        
        height(root)
        return res
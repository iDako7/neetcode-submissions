# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        use bfs
        visit right node first
        if right node, skip left
        if not right node, return left
        """

        q = deque()
        res = []

        if root:
            q.append(root)
        
        while q:
            temp = []
            # iterate all node in queue
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                
                # append left to right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # append the last to res
            res.append(temp[-1])
        

        return res
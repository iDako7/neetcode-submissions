class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        use queue and while loop to traverse

        while queue:
            visited node in queue:
                for child of node, enqueque
        """


        queue = deque()
        res = []

        if root:
            queue.append(root)
        
        while queue:
            # node from same layer add to temp array
            temp = []
            
            # iterate through all the node in same layer
            for i in range(len(queue)):
                # add current node to temp
                node = queue.popleft()
                temp.append(node.val)

                # find child node and append to queue
                if node.left:
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            
            # append temp to res
            res.append(temp)
        
        return res
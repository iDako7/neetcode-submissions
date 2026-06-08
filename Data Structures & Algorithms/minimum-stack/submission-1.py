class MinStack:

    class Node:
        def __init__(self, val, current_min):
            self.val = val
            self.current_min = current_min
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        new_node = MinStack.Node(val, val)  # assume new_min = val for now

        if self.head is not None:
            new_node.current_min = min(val, self.head.current_min)

        new_node.next = self.head  # wire new node to old head
        self.head = new_node       # slide head over

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.current_min
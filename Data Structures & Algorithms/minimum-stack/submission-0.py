class MinStack:

    class Node:
        def __init__(self, val, current_min, next=None):
            self.val = val
            self.current_min = current_min
            self.next = next

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            new_min = val
        else:
            new_min = min(val, self.head.current_min)
        self.head = MinStack.Node(val, new_min, self.head)  # <-- fixed

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.current_min
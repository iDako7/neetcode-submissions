class MyQueue:
    # stack1: a, b, c
    # stack2: c, b, a

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # if s2: popout directly
        # if not: add first

        if not self.s2:
            # add from s1
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s1:
            # add from s1
            while self.s2:
                self.s1.append(s2.pop())
        
        return self.s1[0]
        

    def empty(self) -> bool:
        if (self.s1 or self.s2):
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
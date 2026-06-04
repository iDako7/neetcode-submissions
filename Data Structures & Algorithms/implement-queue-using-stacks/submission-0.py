class MyQueue:

    def __init__(self):
        # two stack, one take in, one take out
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        # if s2 is empty, move item from s1 to s2
        if not self.s2:
            while self.s1:
                item = self.s1.pop()
                self.s2.append(item)
        # otherwise, pop directly from s1
        return self.s2.pop()
        

    def peek(self) -> int:
        # if s2 is empty, move item from s1 to s2
        if not self.s2:
            while self.s1:
                item = self.s1.pop()
                self.s2.append(item)

        # otherwise, return -1 item
        return self.s2[-1]
        

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
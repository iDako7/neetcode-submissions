class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            # number
            if t not in "+/*-":
                temp = int(t)
            elif t == "+":
                temp = stack.pop() + stack.pop()    
            elif t == "*":
                temp = stack.pop() * stack.pop()
            elif t == "/":
                temp = int(stack.pop() / stack.pop())
            stack.append(temp)
        
        return stack[0]
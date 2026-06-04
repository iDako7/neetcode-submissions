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
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                temp = a - b
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                temp = int(a / b)
            stack.append(temp)
        
        return stack[-1]
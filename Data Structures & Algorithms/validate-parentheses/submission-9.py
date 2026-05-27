class Solution:
    def isValid(self, s: str) -> bool:
        # (]
        # ([)]
        # ()]

        # stack to store openning brackets
        opening = []
        closing = { ")" : "(", "]" : "[", "}" : "{" }


        # for each closing character, check if the top of stack is the same type
        for c in s:
            # if opening, add to stack
            if c not in closing:
                opening.append(c)
            
            # if closing, validate it
            else:
                if opening and closing[c] != opening.pop():
                    return False
        return not opening
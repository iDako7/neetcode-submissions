class Solution:
    def isValid(self, s: str) -> bool:
        # create a map to store the opening and closing pair
        # for i in n
            # popout == mapped closing
        # return true

        mapping = {"(": ")", "[" :"]", "{":"}"}

        opening = []
        for c in s:
            if c in mapping:
                opening.append(c)
            else:
                if not opening or mapping[opening.pop()] != c:
                    return False
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # if l or r isn't letter, skip
            # ! error: should check edge case first; syntax error
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1


            # !error forgot to check edge case
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        # all pass, then true
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l and r keep moving inward, until l >= r
            # skip all the invalid letter for l and r
        # return true if all passed
        l = 0
        r = len(s) - 1

        # "a ba"
        while l < r:
            # skip invalid case first
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # validate palindrome
            if s[l].lower() != s[r].lower():
                return False        
            # keep moving inward
            l += 1
            r -= 1
        # all pass, return true  
        return True

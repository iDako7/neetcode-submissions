class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap to trace value and idx
        idx = {}
        res = 0
        
        l = 0
        # iterate through using for loop
        for r in range(len(s)):
            # find duplicate then shrink to avoid duplication
            if s[r] in idx:
                l = idx[s[r]] + 1

            # update max len
            idx[s[r]] = r
            res = max(res, r - l + 1)
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap to trace value and idx
        idx = {}
        res = 0
        
        l = 0
        # iterate through using for loop
        
        for r, val in enumerate(s):
            if val in idx and idx[val] >= l:
                l = idx[val] + 1
            
            idx[val] = r
            res = max(res, r - l + 1)
        return res

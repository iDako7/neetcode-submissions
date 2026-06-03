class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "zxyzxyz"
        seen = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            
            # keep removing the left end item until no duplicate found
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            # always add current item to seen
            seen.add(s[r])
            res = max(res, (r - l + 1))
        return res
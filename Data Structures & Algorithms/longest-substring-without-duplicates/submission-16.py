class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # track whether this item is duplicate
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # check whether s[r] has been seen before
            while s[r] in seen:
                # shrink the sliding window
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res
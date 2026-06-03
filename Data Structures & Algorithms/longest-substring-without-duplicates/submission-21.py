class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen = set

        # for r in len:
            # check whether condition met
            # while duplicate (r in seen):
                # modify seen
                # l += 1
            # modify res with max
        # return res

        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # check condition
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            # modify res
            res = max(res, (r - l + 1))
        return res
                



                
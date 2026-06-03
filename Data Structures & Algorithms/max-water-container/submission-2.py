class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use 2 pointer to find the higher pillar
        
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            # caculate the current area
            area = min(heights[l], heights[r]) * (r - l)
            # modify max area
            res = max(res, area)

            # if left lower, move l
            # else, move r
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        
        return res
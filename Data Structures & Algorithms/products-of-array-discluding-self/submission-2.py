class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
        
        # more than one zero, then every product is 0
        if zero_count > 1:
            return [0] * len(nums)
        
        # calculate product without 0
        # O(n)
        total = 1
        for num in nums:
            if num != 0:
                total *= num
        
        res = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)
        
        return res
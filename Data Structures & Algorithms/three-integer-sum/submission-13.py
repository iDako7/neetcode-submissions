class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for item in nums
            # l = i + 1, r = len -1
            # while l < r, check whether meet the target
        # store different combination of same total
        temp = {}
        
        for i, num in nums.item():
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = num + nums[l] + nums[r]
                

        
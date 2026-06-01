class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first
        # for loop
            # skip duplicate from 1 to n
            # while loop for two sum
                # == target
                    # skip duplicate first
                    # l and r move inward
                # < target, l move inward
                # > target, r move inward
        
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r] + num
                if total == 0:
                    res.append([num, nums[l], nums[r]])

                    # skip future duplicate first
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    # error: Time Limit Exceeded -- should write comment first
                    l += 1
                    r -= 1
                
                elif total <  0:
                    l += 1
                else:
                    r -=1
        return res   

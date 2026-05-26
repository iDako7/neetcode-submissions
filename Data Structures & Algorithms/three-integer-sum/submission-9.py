class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # no duplicate
        # 2 sum + 1

        # sort first
        nums.sort()

        # iterate to unique num to find two sum with target == - num
        res = []
        for i, num in enumerate(nums):
            target = -num

            if nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                # skip duplicate first
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                # verify sum
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                
                # keep moving inward
                l += 1
                r -= 1

        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        # n
        for i in range(len(nums)):
            # Skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            num = nums[i]
            target = 0 - num
            l = i + 1
            r = len(nums) - 1
            
            # n
            while l < r:
                pair = nums[l] + nums[r]
                if pair == target:
                    res.append([nums[i], nums[l], nums[r]])

                    # we need to skip duplicate, then this become palidrone problem
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif pair < target:
                    l += 1
                elif pair > target:
                    r -= 1
        return res


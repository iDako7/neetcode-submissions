class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        # n
        for i in range(len(nums)):
            num = nums[i]
            target = 0 - num
            l = i + 1
            r = len(nums) - 1
            
            # n
            while l < r:
                pair = nums[l] + nums[r]
                if pair == target:
                    temp = [nums[i], nums[l], nums[r]]

                    #  n
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    r -= 1
                elif pair < target:
                    l += 1
                elif pair > target:
                    r -= 1
        return res
#  n nested 3 times, therefore, the time complexity is n^3

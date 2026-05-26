class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        vk = {}
        for i in range(len(nums)-1, -1, -1):
            vk[nums[i]] = i

        nums.sort()

        while l < r:
            # if sum == target, return res
            temp = nums[l] + nums[r]
            if temp == target:
                return [vk[nums[l]], vk[nums[r]]]

            # if less, move l to right
            elif temp < target:
                l += 1

            # if more, move r to left
            elif temp > target:
                r -= 1
        
        return 
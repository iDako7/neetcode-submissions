class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vk = []
        for i in range(len(nums)-1, -1, -1):
            vk.append(tuple((nums[i], i)))

        vk.sort()
        l = 0
        r = len(vk) - 1

        while l < r:
            # if sum == target, return res
            temp = vk[l][0] + vk[r][0]
            if temp == target:
                res = [vk[l][1], vk[r][1]]
                res.sort()
                return res

            # if less, move l to right
            elif temp < target:
                l += 1

            # if more, move r to left
            elif temp > target:
                r -= 1
        
        return 
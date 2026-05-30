class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # calculate prefix for 1 to n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # calculate suffix for n-1 to 1
        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        # product = pre * suffix
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res
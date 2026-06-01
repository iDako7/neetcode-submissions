class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build a prefix
        # build a suffix
        # mutiple them together, then got the result

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # calculate prefix: move forward
        for i in range(1, n, 1):
            prefix[i] = prefix[i-1] * nums[i-1]

        # calculate suffix: move backward
        # error: for j in range(-1, 1, -1):
        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        res = []
        for i in range(n):
            product = prefix[i] * suffix[i]
            res.append(product)
        
        return res
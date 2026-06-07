class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1, 2, 3

        1 + 3 or 2

        1 return 1
        1, 2 return max(1, 2)
        1, 2, 3 return max(1+3, 2)
    
        '''
        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            rob1 = nums[i] + dfs(i+2)
            rob2 = dfs(i+1)
            dp[i]  = max(rob1, rob2)
            return dp[i]
        
        return dfs(0)
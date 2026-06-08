class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [2,9,8,3,6]
        2,   10
        2.      3
          9     3
          9        6
        """
        dp = [-1] * len(nums)

        def dfs(i, flag):
            if i >= len(nums):
                return 0
            
            # start from head and bypass end
            if i == len(nums) - 1 and flag:
                return 0
            
            # whether already calculated
            if dp[i] != -1:
                return dp[i]
            
            rob1 = nums[i] + dfs(i+2, flag)
            rob2 = dfs(i+1, flag)
            return max(rob1, rob2)
        
        rob0 = dfs(0, True)
        rob1 = dfs(1, False)
        return max(rob0, rob1)
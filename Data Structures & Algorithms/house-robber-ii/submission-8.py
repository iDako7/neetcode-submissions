class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [2,9,8,3,6]
        2,   10
        2.      3
          9     3
          9        6
        """
        n = len(nums) 
        dp = []
        for _ in range(n):
            dp.append([-1, -1])

        def dfs(i, flag):
            if i >= n:
                return 0
            
            # start from head and bypass end
            if i == n - 1 and flag:
                return 0
            
            # whether already calculated
            if dp[i][flag] != -1:
                return dp[i][flag]
            
            rob1 = nums[i] + dfs(i+2, flag)
            rob2 = dfs(i+1, flag)
            dp[i][flag] = max(rob1, rob2)
            return dp[i][flag] 
        
        rob0 = dfs(0, 1)
        rob1 = dfs(1, 0)
        return max(rob0, rob1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(houses):
            # Standard House Robber I, top-down
            memo = {}
            def dfs(i):
                if i >= len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(houses[i] + dfs(i + 2), dfs(i + 1))
                return memo[i]
            return dfs(0)

        # Either skip first house or skip last — take the better result
        return max(rob_range(nums[:-1]), rob_range(nums[1:]))
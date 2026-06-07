class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1, 2, 3

        1 + 3 or 2

        1 return 1
        1, 2 return max(1, 2)
        1, 2, 3 return max(1+3, 2)
    
        '''

        def dfs(i):
            if i >= len(nums):
                return 0
            
            rob1 = nums[i] + dfs(i+2)
            rob2 = dfs(i+1)
            return max(rob1, rob2)
        
        return dfs(0)
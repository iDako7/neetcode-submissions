class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1, 0, 2, 3
        # 1, 2, 3, 0
        # l mark 0
        # for r in n:
            # if num is 0: move left pointer to this position
            # if num isn't 0 and l > -1:
                # swap
        
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
        

        

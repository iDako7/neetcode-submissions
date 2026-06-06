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
            # print(f"l is {l}")
            if nums[r] != 0:
                # error: didn't use temp, therefore when fail to pass nums=[1,0,2,0,0,3,4]

                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1

        

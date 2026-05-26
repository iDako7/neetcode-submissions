class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            # if item isn't zero, swap with the lattest 0
            if nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1

            # if 0 continue
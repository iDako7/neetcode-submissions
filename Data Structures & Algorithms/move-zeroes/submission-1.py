class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        count = 0

        for i in range(len(nums)):
            # not 0, add to temp
            if nums[i] != 0:
                temp.append(nums[i])
            else:
                # 0, count but not add
                count += 1
        
        for j in range(count):
            temp.append(0)
        
        nums[:] = temp
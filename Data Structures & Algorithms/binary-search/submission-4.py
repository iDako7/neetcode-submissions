class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # while l < r:
            # mid = (l + r) // 2

            # if target > value of mid:
                # move l to right
            # if target < value:
                # move r to left
            # else:
                # found
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            value = nums[mid]

            # error: didn't add 1 or decrease 1 
            if target > value:
                l = mid + 1
            elif target < value:
                r = mid - 1
            else:
                return mid
        return -1

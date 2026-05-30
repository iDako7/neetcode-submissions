class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # only calculate unique num
        nums_set = set(nums)
        longest = 0

        for num in nums:
            # check whether is the start of the sequence
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    # if true, keep counting until there is no subsequent item in set
                    length += 1
                # modify longest
                longest = max(longest, length)
        
        return longest
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1, 0, 0, 1, 2]
    
        nums.sort()  # sorting makes dedup easy
        result = []

        for i in range(len(nums) - 2):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            j = i + 1

            while j < len(nums):
                complement = -nums[i] - nums[j]

                if complement in seen:
                    result.append([nums[i], complement, nums[j]])
                    # skip duplicate nums[j] values
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1

                seen.add(nums[j])
                j += 1

        return result
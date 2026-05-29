class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num is the key, freq is the value
        # [2,1,1]
        freq = {}

        # calculate frequency by iteration
        for i, num in enumerate(nums):
            freq[num] = 1 + freq.get(num, 0)
            # 2:1 1:2

        # turn map into list, sort by frequency, pop top k number
        rank = []
        for num in freq:
            rank.append((freq[num], num))
        
        rank.sort()
        
        res = []
        # mistakenly put k with len(k)
        for _ in range(k):
            res.append(rank.pop()[1])
        
        # should write return first
        return res
        
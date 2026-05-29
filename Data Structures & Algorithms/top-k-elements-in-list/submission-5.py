class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num : freq
        # [2,1,1]
        freq = {}

        # calculate frequency by iteration
        # {2:1, 1:2}
        for i, num in enumerate(nums):
            freq[num] = 1 + freq.get(num, 0)
    

        # turn map into list, sort by frequency, pop top k number
        # [(1:2)]
        # todo
        rank = []
        for num in freq:
            rank.append((freq[num], num))
        
        # sort by the key? tuple
        rank.sort()
        
        res = []
        # mistakenly put k with len(k)
        for _ in range(k):
            res.append(rank.pop()[1])
        
        # should write return first
        return res
        
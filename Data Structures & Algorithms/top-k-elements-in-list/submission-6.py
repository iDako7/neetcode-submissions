class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create map to calculate frequency
        # num : freq
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # sort by frequency
        # turn map into list to sort
        rank = []
        for num, freq in freq.items():
            rank.append((freq, num))

        rank.sort()

        # return the Kth frequent item
        res = []
        for _ in range(k):
            res.append(rank.pop()[1])
        
        # forgot to return !
        return res
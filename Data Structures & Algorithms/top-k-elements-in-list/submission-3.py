class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # freq is val, num is index
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        rank = []
        for i in count:
            rank.append([count[i], i])
        rank.sort()

        res = []
        for i in range(k):
            res.append(rank.pop()[1])
        
        return res

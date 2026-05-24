class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key: num, val: freq
        count = {}

        # add all element to count
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # flip: key is freq, val is num
        # use list because, list can support sort
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res
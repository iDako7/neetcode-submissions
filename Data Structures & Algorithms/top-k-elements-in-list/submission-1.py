class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency is the value
        count = {}

        # count the freq for each element in the array
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1


        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res
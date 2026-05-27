class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res

        res = [0] * len(temperatures)
        # [30,38,30,40]
        # store indices
        stack = [] 

        for i, t in enumerate(temperatures):
            # find higher temp, then pop item and modify result
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res

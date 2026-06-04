class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 
        n = len(temperatures)
        res = [0] * n
        
        # store a tuple (temperatures and idx)
        stk = []

        
        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t:
                temps, idx = stk.pop()
                res[idx] = i - idx
            
            stk.append((t, i))
        return res

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # initialize calculation information
        # pair = []
        # for idx in n:
            # add positon, speed and time as a tuple
            # sort pait with reverse order
        
        # res = 0
        # for car in pairs:
            # if car is slowwer, individual == one fleet:
                # res += 1
                # modify max time
        # return res


        pairs = []

        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            t = (target - p) / s
            pairs.append((p, t))
        pairs.sort(reverse=True)
        
        res = 0
        max_time = 0

        for car in pairs:
            p, t = car

            if t > max_time:
                res += 1
                max_time = t
        return res
            
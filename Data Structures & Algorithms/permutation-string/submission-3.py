class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq1 and freq2: use list to store frequency
        # for i in n1:
            # freq1.append(item from s1)
            # freq2.append(item from s1)
        # check freq1 == freq2

        # fixed size window
        # for i in n2:
            # add new item from s2
            # remove the head item from s2
        # check freq1 == freq2

        # return False

        n1 = len(s1)
        n2 = len(s2)

        # missed this
        if n1 > n2:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        

        for i in range(n1):
            freq1[ord(s1[i]) - ord('a')] += 1 # [1, 1, 1]
            freq2[ord(s2[i]) - ord('a')] += 1 # [0, 0, 1, ... 1, ... 1]
        
        if freq1 == freq2:
            return True
        
        for i in range(n1, n2):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - n1]) - ord('a')] -= 1
            if freq1 == freq2:
                return True
        return False

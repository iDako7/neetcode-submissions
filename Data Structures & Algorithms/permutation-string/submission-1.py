class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use list to store freq and compar
        # check if len_s1 > s2
        # for i in s1:
            # calculate freq for s1
            # do increment scan for s2
        # if freq_s1 == freq_s2
        
        # for loop, fix lenghth scan for s2
        # if freq_s1 == freq_s2

        # return false

        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:
            return False
        
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        for i in range(n1):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1
        
        if freq_s1 == freq_s2:
            return True
        
        for i in range(n1, n2):
            freq_s2[ord(s2[i]) - ord('a')] += 1
            freq_s2[ord(s2[i - n1]) - ord('a')] -= 1
            
            if freq_s1 == freq_s2:
                return True
        
        return False





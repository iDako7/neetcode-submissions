class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # create two map to calculate
        count1 = {}
        count2 = {}

        # initialize two map
        for i in range(len(s)):
            count1[s[i]] = 1 + count1.get(s[i], 0)
            count2[t[i]] = 1 + count2.get(t[i], 0)

        # compare
        return count1 == count2
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  l = 0
        # for r in len:
            # condition = len_of_cur_arr - max_frequency > k
            # while condition not meet:
                # keep shrink the array from left to right
            
            # calculate the current max len
            # modify the res
        # return res

        l = 0 
        freq = {}
        res = 0
        max_freq = 0

        for r in range(len(s)):
            # update frequency
            freq[s[r]] = 1 + freq.get(s[r], 0)
             
            max_freq = max(freq[s[r]], max_freq)

            # check whehter we meet the condition
            # s = "AA|ABBBB"
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
                max_freq = max(freq[s[r]], max_freq)
            
            res = max(res, (r - l + 1))
        return res

            

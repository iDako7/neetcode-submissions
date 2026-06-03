class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "AAABABB"
        l = 0
        max_freq = 0
        freq = {}
        res = 0

        # increase r always
        for r in range(len(s)):
            # modify the frequency of the character
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            # modify the max freq
            max_freq = max(max_freq, freq[s[r]])

            # if this is an invalid string, then shrink
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            # modify the res
            res = max(res, r - l + 1)
        return res
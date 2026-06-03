class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0   # max freq of any single char seen so far
        freq = {}
        res = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(maxf, freq[s[r]])      # ← your "res" line

            while (r - l + 1) - maxf > k:    # ← what you were filling in
                freq[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
        return res
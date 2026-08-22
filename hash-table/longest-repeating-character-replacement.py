class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        mlen = 0
        maxfreq = 0
      
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] +=1
            else:
                freq[s[r]] = 1

            maxfreq = max(maxfreq, freq[s[r]])

            while (r-l+1) - maxfreq > k:
                freq[s[l]] -=1
                l +=1
            mlen = max(mlen, r-l+1)
        
        return mlen

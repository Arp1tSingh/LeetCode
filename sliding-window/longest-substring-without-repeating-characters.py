class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        chars = set()
        slen = 0

        for i in range(len(s)):
            if s[i] not in chars:
                chars.add(s[r])
                if slen< r-l+1:
                    slen = r-l+1
                r +=1
            else:
                chars.remove(s[l])
                l+=1
        return slen
            

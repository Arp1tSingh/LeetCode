class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            count = {}
            for ch in s:
                if ch in count:
                    count[ch] = count[ch]+1
                else:
                    count[ch] = 1
            
            for ch in t:
                if ch not in count:
                    return ch
                
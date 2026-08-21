class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        mcount = 0
        l = 0
        count = 0

        for r in range(len(s)):
            if r<k:
                if s[r] in vowels:
                    count +=1
                    mcount = count

            else:
                if s[r] in vowels:
                    count +=1
                if s[l] in vowels:
                    count -=1
                l += 1
                mcount = max(mcount,count)
        return mcount

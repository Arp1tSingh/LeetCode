class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = k
        l = 0
        mlen = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                continue
            elif nums[r] == 0 and count >0:
                count-=1
                
            elif nums[r] == 0 and count==0:
                clen = r-l
                mlen = max(clen,mlen)
                while nums[l] != 0:
                    l+=1
                l+=1
        return mlen
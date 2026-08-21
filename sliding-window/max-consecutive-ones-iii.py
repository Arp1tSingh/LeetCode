class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = k
        l = 0
        mlen = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                mlen = max(r-l+1,mlen)
                continue
            elif nums[r] == 0 and count >0:
                count-=1
                mlen = max(r-l+1,mlen)
            elif nums[r] == 0 and count==0:
                
                while nums[l] != 0:
                    l+=1
                l+=1
                mlen = max(r-l+1,mlen)
                
        return mlen
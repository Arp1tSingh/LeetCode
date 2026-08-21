class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = 0
        msum = 0

        while r<k:
            msum += nums[r]
            r+=1
        while r<len(nums):
            nsum = (msum - nums[l]) + nums[r]
            msum = max(nsum,msum)
            r+=1
            l+=1
        return msum/k
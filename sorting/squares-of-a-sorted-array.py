class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        snums = []
        l = 0
        r = len(nums)-1
        ls = 0
        rs = 0
        while l<=r:
           ls = nums[l]**2
           rs = nums[r]**2
           if ls>=rs:
               snums.insert(0,ls)
               l+=1
           else:
               snums.insert(0,rs)
               r-=1
        
        return snums
        
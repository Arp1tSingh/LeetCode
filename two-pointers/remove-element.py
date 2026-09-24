class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        mlen = len(nums)
        
        while k<mlen:
            if nums[k] == val:
                nums.remove(val)
                mlen -=1
            else:
                k+=1
        
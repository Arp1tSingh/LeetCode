class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #implementing selection sort [ O(n^2)]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        
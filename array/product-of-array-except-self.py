class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l1 = [1] * n
        l2 = [1] * n
        
        left = 1
        for i in range(n):
            l1[i] = left
            left = left*nums[i]
            
        right = 1
        for i in range(n-1,-1,-1):
            l2[i] = right
            right = right*nums[i]
        
        for i in range(n):
            l1[i] = l1[i]*l2[i]
        return l1
        
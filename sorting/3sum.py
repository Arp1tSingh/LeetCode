class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return []

        array = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                Sum = nums[i] + nums[left] + nums[right]

                if Sum == 0:
                    array.append([nums[i], nums[left], nums[right]])

                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    
                    left += 1
                    right -= 1

                elif Sum > 0:
                    right -= 1

                elif Sum < 0:
                    left += 1

        return array
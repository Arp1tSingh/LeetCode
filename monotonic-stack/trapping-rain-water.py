class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        maxleft = height[0]
        right = len(height)-1
        maxright = height[-1]
        count = 0

        while left<right:
            if height[left]<=height[right]:
                left +=1
                x = maxleft - height[left]
                if x>0:
                    count += x
                if height[left] > maxleft:
                    maxleft = height[left]
            
            else:
                right -=1
                x = maxright - height[right]
                if x>0:
                    count += x
                if height[right] > maxright:
                    maxright = height[right]
        return count          


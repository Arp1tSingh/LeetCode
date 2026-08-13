class Solution:
    def maxArea(self, height: List[int]) -> int:
        mw = 0
        left =0
        right = len(height)-1
        while left < right :
            x = (right-left)*min(height[left],height[right])
            if x>mw:
                mw = x
            if height[left]< height[right] :
                left +=1
            elif height[left]> height[right] :
                right -=1
            else:
                right -=1
        return mw
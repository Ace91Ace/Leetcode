class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        
        tw = 0
        left, right = 0, len(height) - 1
        lm, rm = 0, 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= lm:
                    lm = height[left]
                else:
                    tw += lm - height[left]
                left += 1
            else:
                if height[right] >= rm:
                    rm = height[right]
                else:
                    tw += rm - height[right]
                right -= 1
        
        return tw


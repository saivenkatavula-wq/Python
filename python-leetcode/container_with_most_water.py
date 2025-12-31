class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            hi = height[left]
            hj = height[right]
            if hi < hj:
                area = hi * (right-left)
                left += 1
            else:
                area = hj * (right-left)
                right -= 1
            if area > max_area:
                max_area = area
        return max_area
        

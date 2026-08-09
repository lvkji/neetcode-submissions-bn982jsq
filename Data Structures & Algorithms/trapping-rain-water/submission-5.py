class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        totalWater = 0
        while left < right:
            if height[left] < height[right]:
                left+=1
                leftMax = max(leftMax,height[left])
                totalWater += leftMax - height[left]
            elif height[left] >= height[right]:
                right-=1
                rightMax = max(rightMax,height[right])
                totalWater += rightMax - height[right]
        return totalWater
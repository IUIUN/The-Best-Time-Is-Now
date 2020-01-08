class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        current_left, current_right, res = 0, len(height) - 1, 0
        max_left, max_right = height[current_left], height[current_right]
        while(current_left < current_right):
            max_left = max(height[current_left], max_left)
            max_right = max(height[current_right], max_right)
            if height[current_left] < height[current_right]:
                res += max_left - height[current_left]
                current_left += 1
            else:
                res += max_right -height[current_right]
                current_right -= 1
        return res
        
"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        r = len(height) - 1
        max_area = 0
        while left != r:
            area = (r - left) * min(height[left], height[r])
            max_area = max(area, max_area)
            if height[left] < height[r]:
                left += 1
            else:
                r -= 1
        return max_area

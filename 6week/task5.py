"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/description/
"""


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left, right = 0, len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        return arr[left : left + k]

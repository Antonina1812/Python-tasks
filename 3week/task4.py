"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        r = len(arr) - 1
        while left <= r:
            m = left + (r - left) // 2
            if arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
                return m
            if arr[m - 1] <= arr[m]:
                left = m
            elif arr[m - 1] >= arr[m]:
                r = m

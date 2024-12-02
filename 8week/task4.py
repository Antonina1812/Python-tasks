"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/sliding-window-median/description/
"""


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        def find_median(window):
            sorted_window = sorted(window)
            n = len(sorted_window)
            if n % 2 == 1:
                return sorted_window[n // 2]
            else:
                return (sorted_window[n // 2 - 1] + sorted_window[n // 2]) / 2

        medians = []
        for i in range(len(nums) - k + 1):
            window = nums[i : i + k]
            median = find_median(window)
            medians.append(median)

        return medians


# не работает с большими массивами

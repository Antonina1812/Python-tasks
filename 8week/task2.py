"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/sliding-window-maximum/description/
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []

        deq = deque()
        max_nums = []

        for i in range(len(nums)):
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            if i >= k - 1:
                max_nums.append(nums[deq[0]])

        return max_nums

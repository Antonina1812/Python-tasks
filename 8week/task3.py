"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
"""


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_length = float("inf")

        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += nums[end]
                if current_sum >= k:
                    min_length = min(min_length, end - start + 1)
                    break

        return min_length if min_length != float("inf") else -1


# не работает на больших массивах

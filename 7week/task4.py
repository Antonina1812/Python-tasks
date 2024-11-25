"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum_count = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            if current_sum - goal in prefix_sum_count:
                count += prefix_sum_count[current_sum - goal]

            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1

        return count

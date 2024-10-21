"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_sequence = 0
        seen = set(nums)

        for num in nums:
            if num - 1 not in seen:
                current_num = num
                current_sequence = 1

                while current_num + 1 in seen:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

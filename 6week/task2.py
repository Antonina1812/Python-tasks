"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        length = 0

        n = len(nums)
        if n < 3:
            return 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                length += 1
                count += length
            else:
                length = 0

        return count

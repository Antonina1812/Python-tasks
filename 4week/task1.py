"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/next-permutation/description/
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        def Reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        Reverse(nums, i + 1)

"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findPosition(nums, target, leftBias):
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    i = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i

        start = findPosition(nums, target, True)
        end = findPosition(nums, target, False)
        return [start, end]

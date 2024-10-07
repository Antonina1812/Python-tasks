"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        r = len(numbers) - 1
        k = []
        while left != r:
            if numbers[left] + numbers[r] == target:
                k.append(left + 1)
                k.append(r + 1)
                return k
            elif numbers[left] + numbers[r] > target:
                r -= 1
            else:
                left += 1

"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/product-of-array-except-self/description/
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1]
        for i in range(0, len(nums) - 1):
            ans.append(ans[-1] * nums[i])

        cur = 1
        for i in range(len(nums) - 2, -1, -1):
            cur *= nums[i + 1]
            ans[i] *= cur
        return ans

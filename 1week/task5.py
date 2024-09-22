"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/largest-number/description/
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""

        if max(nums) == 0:
            return '0'

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                num1 = int(str(nums[i]) + str(nums[j]))
                num2 = int(str(nums[j]) + str(nums[i]))
                if num1 < num2:
                    nums[i], nums[j] = nums[j], nums[i]
        for i in nums:
            res = res + str(i)
        return res



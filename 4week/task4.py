"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/combination-sum/description/
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(candidates, target, start, current, result):
            if target < 0:
                return
            elif target == 0:
                result.append(current[:])
            else:
                for i in range(start, len(candidates)):
                    current.append(candidates[i])
                    backtrack(candidates, target - candidates[i], i, current, result)
                    current.pop()

        result = []
        backtrack(candidates, target, 0, [], result)
        return result

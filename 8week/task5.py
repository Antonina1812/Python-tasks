"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/grumpy-bookstore-owner/description/
"""


class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        n = len(customers)
        baseline_satisfied = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        max_additional_satisfied = 0
        current_additional_satisfied = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]

        max_additional_satisfied = current_additional_satisfied

        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]

            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]

            max_additional_satisfied = max(
                max_additional_satisfied, current_additional_satisfied
            )

        return baseline_satisfied + max_additional_satisfied

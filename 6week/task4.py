"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description/
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1 > len_s2:
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len_s1])
        if s1_count == s2_count:
            return True

        for i in range(len_s1, len_s2):
            s2_count[s2[i]] += 1
            s2_count[s2[i - len_s1]] -= 1

            if s2_count[s2[i - len_s1]] == 0:
                del s2_count[s2[i - len_s1]]

            if s1_count == s2_count:
                return True

        return False

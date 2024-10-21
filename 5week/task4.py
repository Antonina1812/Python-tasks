"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/group-anagrams/description/
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if not (sorted_word in words):
                words[sorted_word] = []
            words[sorted_word].append(i)

        return list(words.values())

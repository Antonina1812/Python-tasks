"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/group-anagrams/description/
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if not (sorted_word in words):
                words[sorted_word] = []
            words[sorted_word].append(i)

        return list(words.values())


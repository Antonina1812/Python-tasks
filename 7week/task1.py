"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0

        max_length = 0
        unique_chars = len(set(s))

        for current_unique in range(1, unique_chars + 1):
            char_count = {}
            left = 0
            total_unique = 0
            valid_unique = 0

            for right in range(len(s)):
                if s[right] in char_count:
                    char_count[s[right]] += 1
                else:
                    char_count[s[right]] = 1

                if char_count[s[right]] == 1:
                    total_unique += 1
                if char_count[s[right]] == k:
                    valid_unique += 1

                while total_unique > current_unique:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        total_unique -= 1
                    if char_count[s[left]] == k - 1:
                        valid_unique -= 1
                    left += 1

                if total_unique == current_unique and total_unique == valid_unique:
                    max_length = max(max_length, right - left + 1)

        return max_length

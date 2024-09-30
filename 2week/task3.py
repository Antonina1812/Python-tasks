"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_freq = 0
        freq_map = {}
        left = 0

        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            max_freq = max(max_freq, freq_map[s[right]])

            while right - left + 1 - max_freq > k:
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == 0:
                    del freq_map[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

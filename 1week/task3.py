"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = {}
        l = 0

        for r in range(len(s)):
            l = max(l, chars.get(s[r], 0)) #Обновляем левую границу подстроки. Если символ s[r] уже встречался, то левая граница должна быть максимум между текущим l и последним индексом этого символа плюс 1. Если символ еще не встречался, то chars.get(s[r], 0) вернет 0, и l останется прежним
            max_len = max(max_len, r - l + 1)
            chars[s[r]] = r + 1

        return max_len


"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        substr = ""
        max_sub = s[0]

        def get_palindrom(l, r, substr):

            while l <= r and l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break

                if (r - l + 1) > len(substr):
                    substr = s[l:r+1]
                l -= 1
                r += 1
            return substr

        for i in range(len(s)):
            str1 = get_palindrom(i, i, substr)
            str2 = get_palindrom(i, i + 1, substr)

            if len(str1) > len(max_sub):
                max_sub = str1
            if len(str2) > len(max_sub):
                max_sub = str2

        return max_sub
"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = ['']
        if not digits:
            return []

        list_of_digits = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        for digit in digits:
            new_res = []
            for i in res:
                for j in list_of_digits[digit]:
                    new_res.append(i + j)
            res = new_res

        return res
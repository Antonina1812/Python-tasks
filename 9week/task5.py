"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees-ii/description/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n == 0:
            return []

        def generate_trees_help(start, end):
            if start > end:
                return [None]

            all_trees = []
            for root_val in range(start, end + 1):
                left_subtrees = generate_trees_help(start, root_val - 1)
                right_subtrees = generate_trees_help(root_val + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return generate_trees_help(1, n)

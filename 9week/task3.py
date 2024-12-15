"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/recover-binary-search-tree/description/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None

        def inorder_traversal(node):
            nonlocal first, second, prev
            if not node:
                return

            inorder_traversal(node.left)

            if prev and node.val < prev.val:
                if not first:
                    first = prev
                second = node

            prev = node
            inorder_traversal(node.right)

        inorder_traversal(root)

        if first and second:
            first.val, second.val = second.val, first.val

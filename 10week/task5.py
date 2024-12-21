"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
"""


from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def buildBST(arr, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(arr[mid])
            root.left = buildBST(arr, start, mid - 1)
            root.right = buildBST(arr, mid + 1, end)
            return root

        return buildBST(arr, 0, len(arr) - 1)

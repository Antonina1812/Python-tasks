"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
"""


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {value: index for index, value in enumerate(inorder)}
    
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
            
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            root_index = inorder_index_map[root_val]
            
            left_size = root_index - in_start
            
            root.left = build(in_start, root_index - 1, post_start, post_start + left_size - 1)
            root.right = build(root_index + 1, in_end, post_start + left_size, post_end - 1)
            
            return root
        
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
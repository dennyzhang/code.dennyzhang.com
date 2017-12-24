#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
##    ,-----------
##    | Given a binary tree, flatten it to a linked list in-place.
##    | 
##    | For example,
##    | Given
##    | 
##    |          1
##    |         / \
##    |        2   5
##    |       / \   \
##    |      3   4   6
##    | The flattened tree should look like:
##    |    1
##    |     \
##    |      2
##    |       \
##    |        3
##    |         \
##    |          4
##    |           \
##    |            5
##    |             \
##    |              6
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-28 21:01:16>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        ## Idea: DFS for pre-order traversal
        ## Complexity: Time O(n), Space O(n)
        self._flatten(root)

    def _flatten(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode: last node in the chain
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root

        root_right = root.right
        q = None
        if root.left:
            q = self._flatten(root.left)
            q.right = root.right
            root.right = root.left
            root.left = None

        if root_right:
            q = self._flatten(root.right)
            
        return q

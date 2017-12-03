#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/trim-a-binary-search-tree/description/
##    ,-----------
##    | Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
##    | 
##    | Example 1:
##    | Input: 
##    |     1
##    |    / \
##    |   0   2
##    | 
##    |   L = 1
##    |   R = 2
##    | 
##    | Output: 
##    |     1
##    |       \
##    |        2
##    | Example 2:
##    | Input: 
##    |     3
##    |    / \
##    |   0   4
##    |    \
##    |     2
##    |    /
##    |   1
##    | 
##    |   L = 1
##    |   R = 3
##    | 
##    | Output: 
##    |       3
##    |      / 
##    |    2   
##    |   /
##    |  1
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        ## Basic Idea: recursive pre-order traseveral
        ## Complexity:
        ## Assumptions: No duplicate elements in the BST
        ## 
        if root is None:
            return None

        value = root.val
        if value >= L and value <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root

        if value < L:
            # left tree won't be qualified
            return self.trimBST(root.right, L, R)

        if value > R:
            # right tree won't be qualified
            return self.trimBST(root.left, L, R)

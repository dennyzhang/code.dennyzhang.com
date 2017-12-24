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
##     https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
##    ,-----------
##    | Given a binary tree, find its minimum depth.
##    | 
##    | The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-12 10:59:16>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## Idea: DFS
        ## Complexity:
        depth = None
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            return 1
        elif (root.left is None):
            return self.minDepth(root.right)+1
        elif (root.right is None):
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left)+1, self.minDepth(root.right)+1)

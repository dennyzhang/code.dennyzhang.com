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
##     https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
##    ,-----------
##    | Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
##    | 
##    | An example is the root-to-leaf path 1->2->3 which represents the number 123.
##    | 
##    | Find the total sum of all root-to-leaf numbers.
##    | 
##    | For example,
##    | 
##    |     1
##    |    / \
##    |   2   3
##    | The root-to-leaf path 1->2 represents the number 12.
##    | The root-to-leaf path 1->3 represents the number 13.
##    | 
##    | Return the sum = 12 + 13 = 25.
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-03 10:14:57>
##-------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ## Idea: BFS
        ## Complexity:
        res = 0
        if root is None:
            return 0
        queue = []
        queue.append((root, root.val))
        while len(queue) != 0:
            (node, value) = queue[0]
            del queue[0]
            if node.left:
                queue.append((node.left, value*10 + node.left.val))
            if node.right:
                queue.append((node.right, value*10 + node.right.val))
            # left node
            if node.left is None and node.right is None:
                res += value
        return res

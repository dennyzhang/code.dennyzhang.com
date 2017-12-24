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
##     https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
##    ,-----------
##    | You need to find the largest value in each row of a binary tree.
##    | 
##    | Example:
##    | Input: 
##    | 
##    |           1
##    |          / \
##    |         3   2
##    |        / \   \  
##    |       5   3   9 
##    | 
##    | Output: [1, 3, 9]
##    `-----------
##
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## Ideas: BFS
        ## Complexity
        if root is None:
            return []
        res = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            length = len(queue)
            max_value = queue[0].val
            for i in range(1, length):
                if queue[i].val > max_value:
                    max_value = queue[i].val
            res.append(max_value)
            for i in range(0, length):
                element = queue[0]
                del queue[0]
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        return res

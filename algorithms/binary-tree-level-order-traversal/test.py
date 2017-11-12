#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags:
## Description:
##     https://leetcode.com/problems/binary-tree-level-order-traversal/description/
##    ,-----------
##    | Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
##    | 
##    | For example:
##    | Given binary tree [3,9,20,null,null,15,7],
##    |     3
##    |    / \
##    |   9  20
##    |     /  \
##    |    15   7
##    | return its level order traversal as:
##    | [
##    |   [3],
##    |   [9,20],
##    |   [15,7]
##    | ]
##    `-----------
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ## Baisc Idea: BFS
        ## Complexity: Time O(n), Space O(n): width
        if root is None:
            return []
        res = []
        queue = []
        queue.append(root)
        while len(queue) != 0:
            length = len(queue)
            level_elements = []
            for i in xrange(length):
                element = queue[0]
                del queue[0]
                level_elements.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(level_elements)
        return res
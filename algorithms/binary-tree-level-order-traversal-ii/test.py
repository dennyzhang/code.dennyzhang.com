#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo
## Description:
##     https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
##    ,-----------
##    | Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
##    | 
##    | For example:
##    | Given binary tree [3,9,20,null,null,15,7],
##    |     3
##    |    / \
##    |   9  20
##    |     /  \
##    |    15   7
##    | return its bottom-up level order traversal as:
##    | [
##    |   [15,7],
##    |   [9,20],
##    |   [3]
##    | ]
##    `-----------
##
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-11-03 10:14:57>
##-------------------------------------------------------------------
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ## Idea: BFS
        ## Complexity:
        res = []
        if root is None:
            return res
        queue = []
        queue.append(root)
        while len(queue) != 0:
            length = len(queue)
            l = []
            for i in xrange(length):
                l.append(queue[i].val)
            res.insert(0, l)

            for i in xrange(length):
                element = queue[0]
                del queue[0]
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        return res

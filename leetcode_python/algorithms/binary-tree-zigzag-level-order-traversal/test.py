#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <contact@dennyzhang.com>
## Tags:
## Description:
##     https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
##    ,-----------
##    | Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
##    | 
##    | For example:
##    | Given binary tree [3,9,20,null,null,15,7],
##    |     3
##    |    / \
##    |   9  20
##    |     /  \
##    |    15   7
##    | return its zigzag level order traversal as:
##    | [
##    |   [3],
##    |   [20,9],
##    |   [15,7]
##    | ]
##    `-----------
##
##
## Basic Idea:
## Complexity:
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ## Idea: BFS, use left_to_right(boolen) for level traversal direction
        ## Complexity: Time O(n), Space O(k)
        if root is None:
            return []
        res = []
        queue = []
        queue.append(root)
        left_to_right = True
        while len(queue) != 0:
            length = len(queue)
            level_element = []
            for i in xrange(length):
                element = queue[0]
                del queue[0]
                if left_to_right is True:
                    level_element.append(element.val)
                else:
                    level_element.insert(0, element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(level_element)
            left_to_right = not left_to_right
        return res

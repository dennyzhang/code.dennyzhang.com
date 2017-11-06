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
##     https://leetcode.com/problems/path-sum-ii/description/
##    ,-----------
##    | Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
##    | 
##    | For example:
##    | Given the below binary tree and sum = 22,
##    |               5
##    |              / \
##    |             4   8
##    |            /   / \
##    |           11  13  4
##    |          /  \    / \
##    |         7    2  5   1
##    | return
##    | [
##    |    [5,4,11,2],
##    |    [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ## Idea: Use DFS recursive
        ## Complexity: Time O(n), Space O(log(n)*k). k is width of the tree
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        res = []
        if root.left:
            list_value = self.pathSum(root.left, sum - root.val)
            for value in list_value:
                value.insert(0, root.val)
                res.append(value)
        if root.right:
            list_value = self.pathSum(root.right, sum - root.val)
            for value in list_value:
                value.insert(0, root.val)
                res.append(value)
        return res